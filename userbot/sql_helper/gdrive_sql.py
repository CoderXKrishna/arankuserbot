# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# arankUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by CoderXKrishna@Github.

# This file is part of: https://github.com/CoderXKrishna/arankuserbot
# and is released under the "GNU v3.0 License Agreement".

# Please see: https://github.com/CoderXKrishna/arankuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

from sqlalchemy import Column, String

from . import BASE, SESSION


class Gdrive(BASE):
    __tablename__ = "arankgdrive"
    arank = Column(String(50), primary_key=True)

    def __init__(self, arank):
        self.arank = arank


Gdrive.__table__.create(checkfirst=True)


def is_folder(folder_id):
    try:
        return SESSION.query(Gdrive).filter(Gdrive.arank == str(folder_id))
    except BaseException:
        return None
    finally:
        SESSION.close()


def gparent_id(folder_id):
    adder = SESSION.query(Gdrive).get(folder_id)
    if not adder:
        adder = Gdrive(folder_id)
    SESSION.add(adder)
    SESSION.commit()


def get_parent_id():
    try:
        return SESSION.query(Gdrive).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def rmparent_id(folder_id):
    if note := SESSION.query(Gdrive).filter(Gdrive.arank == folder_id):
        note.delete()
        SESSION.commit()
