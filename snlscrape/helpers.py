import datetime
import unidecode

# (The classes in this module are really just acting as namespaces.)


class Aid(object):
    UNKNOWN = 'UNK'

    @staticmethod
    def asciify(name):
        """Make a canonical ascii version of an actor's name.
        Sorry No\xc3\xabl Wells.
        """
        return unidecode.unidecode(name)


class Tid(object):

    @staticmethod
    def to_date(tid):
        year, month, day = map(int, [tid[:4], tid[4:6], tid[6:8]])
        return datetime.date(year, month, day)


class Sid(object):

    @staticmethod
    def from_date(date):
        assert date.month != 8
        # Seasons start around sept-oct, and usually end around may, though there's
        # at least one case that ends in july.
        early = date.month <= 7
        sid = 1 + (date.year - 1975)
        if early:
            sid -= 1
        return sid

    @staticmethod
    def from_year(year):
        """Sometimes snlarchive gives a single year to represent a season (e.g. in the
        season urls). It always refers to the year in which the season starts.
        """
        return 1 + (year - 1975)

    @classmethod
    def from_tid(cls, tid):
        date = Tid.to_date(tid)
        return cls.from_date(date)

    @classmethod
    def from_epid(cls, epid):
        date = Epid.to_date(epid)
        return cls.from_date(date)


class Epid(object):

    @staticmethod
    def from_tid(tid):
        epid_len = 4 + 2 + 2
        return tid[:epid_len]

    @staticmethod
    def to_date(epid):
        year, month, day = map(int, [epid[:4], epid[4:6], epid[6:8]])
        return datetime.date(year, month, day)
