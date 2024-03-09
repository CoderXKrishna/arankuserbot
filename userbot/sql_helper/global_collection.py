# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# arankUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by CoderXKrishna@Github.

# This file is part of: https://github.com/CoderXKrishna/arankuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/CoderXKrishna/arankuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import threading

from sqlalchemy import Column, PickleType, UnicodeText, distinct, func

from . import BASE, SESSION


class arank_GlobalCollection(BASE):
    __tablename__ = "arank_globalcollection"
    keywoard = Column(UnicodeText, primary_key=True)
    contents = Column(PickleType, primary_key=True, nullable=False)

    def __init__(self, keywoard, contents):
        self.keywoard = keywoard
        self.contents = tuple(contents)

    def __repr__(self):
        return f"<arank Global Collection lists '{self.contents}' for {self.keywoard}>"

    def __eq__(self, other):
        return (
            isinstance(other, arank_GlobalCollection)
            and self.keywoard == other.keywoard
            and self.contents == other.contents
        )


arank_GlobalCollection.__table__.create(checkfirst=True)

arank_GLOBALCOLLECTION = threading.RLock()


class COLLECTION_SQL:
    def __init__(self):
        self.CONTENTS_LIST = {}


COLLECTION_SQL_ = COLLECTION_SQL()


def add_to_collectionlist(keywoard, contents):
    with arank_GLOBALCOLLECTION:
        keyword_items = arank_GlobalCollection(keywoard, tuple(contents))

        SESSION.merge(keyword_items)
        SESSION.commit()
        COLLECTION_SQL_.CONTENTS_LIST.setdefault(keywoard, set()).add(tuple(contents))


def rm_from_collectionlist(keywoard, contents):
    with arank_GLOBALCOLLECTION:
        if keyword_items := SESSION.query(arank_GlobalCollection).get(
            (keywoard, tuple(contents))
        ):
            if tuple(contents) in COLLECTION_SQL_.CONTENTS_LIST.get(keywoard, set()):
                COLLECTION_SQL_.CONTENTS_LIST.get(keywoard, set()).remove(
                    tuple(contents)
                )
            SESSION.delete(keyword_items)
            SESSION.commit()
            return True

        SESSION.close()
        return False


def is_in_collectionlist(keywoard, contents):
    with arank_GLOBALCOLLECTION:
        keyword_items = COLLECTION_SQL_.CONTENTS_LIST.get(keywoard, set())
        return any(tuple(contents) == list1 for list1 in keyword_items)


def del_keyword_collectionlist(keywoard):
    with arank_GLOBALCOLLECTION:
        keyword_items = (
            SESSION.query(arank_GlobalCollection.keywoard)
            .filter(arank_GlobalCollection.keywoard == keywoard)
            .delete()
        )
        COLLECTION_SQL_.CONTENTS_LIST.pop(keywoard)
        SESSION.commit()


def get_item_collectionlist(keywoard):
    return COLLECTION_SQL_.CONTENTS_LIST.get(keywoard, set())


def get_collectionlist_items():
    try:
        chats = SESSION.query(arank_GlobalCollection.keywoard).distinct().all()
        return [i[0] for i in chats]
    finally:
        SESSION.close()


def num_collectionlist():
    try:
        return SESSION.query(arank_GlobalCollection).count()
    finally:
        SESSION.close()


def num_collectionlist_item(keywoard):
    try:
        return (
            SESSION.query(arank_GlobalCollection.keywoard)
            .filter(arank_GlobalCollection.keywoard == keywoard)
            .count()
        )
    finally:
        SESSION.close()


def num_collectionlist_items():
    try:
        return SESSION.query(
            func.count(distinct(arank_GlobalCollection.keywoard))
        ).scalar()
    finally:
        SESSION.close()


def __load_item_collectionlists():
    try:
        chats = SESSION.query(arank_GlobalCollection.keywoard).distinct().all()
        for (keywoard,) in chats:
            COLLECTION_SQL_.CONTENTS_LIST[keywoard] = []

        all_groups = SESSION.query(arank_GlobalCollection).all()
        for x in all_groups:
            COLLECTION_SQL_.CONTENTS_LIST[x.keywoard] += [x.contents]

        COLLECTION_SQL_.CONTENTS_LIST = {
            x: set(y) for x, y in COLLECTION_SQL_.CONTENTS_LIST.items()
        }

    finally:
        SESSION.close()


__load_item_collectionlists()
