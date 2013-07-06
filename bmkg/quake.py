from xml.etree import ElementTree as ET
import urllib2

import settings


class Quake(object):
    """
    This class is used to fetch data about Earth Quakes that was/just happened
    in Indonesia.
    """

    def latest_quakes(self, single=False, lang='ID'):
        """
        Fetch latest Quakes.
        Usage:
        ---------------------------------------------------
        q = Quake()

        quakes = q.latest_quakes()
        --- OR ---
        # To return the latest quake and in english.
        quakes = q.latest_quakes(single=True, lang='EN')

        return values:
        [{
            'latitude': '1.63 LU',
            'points': ['126.35,1.63'],
            'time': '12:11:31 WIB',
            'date': '14-Apr-13',
            'magnitude': '5.0 SR',
            'area': '133 km TimurLaut BITUNG-SULUT',
            'symbol': '../imagesSWF/m2.swf',
            'longitude': '126.35 BT'
        }]
        ---------------------------------------------------
        """
        url = settings.LATEST_QUAKES_DATA_ID
        if lang == 'EN':
            url = settings.LATEST_QUAKES_DATA_ID

        req = urllib2.urlopen(url)
        tree = ET.fromstring(req.read())

        if single: quakes = map(self._mapper, [tree.find('gempa')])
        else: quakes = map(self._mapper, tree.findall('gempa'))
        return quakes

    def _mapper(self, el_quake):
        """
        Return the quake data in a dictionary format.
        """
        quake = {
            'date': el_quake.find('Tanggal').text,
            'time': el_quake.find('Jam').text,
            'points': [coord.text for coord in el_quake.find('point').findall('coordinates')],
            'latitude': el_quake.find('Lintang').text,
            'longitude': el_quake.find('Bujur').text,
            'magnitude': el_quake.find('Magnitude').text,
            'area': el_quake.find('Wilayah').text,
            # Don't exactly know what is this 'symbol' refer to :)
            'symbol': el_quake.find('_symbol').text,
        }
        return quake


if __name__ == '__main__':
    q = Quake()

    # All Quakes
    print '--------------- Recently Earth Quake ------------------'
    quakes = q.latest_quakes()
    print quakes

    # Latest Quakes
    print '--------------- Latest Earth Quake ------------------'
    quakes = q.latest_quakes(single=True)
    print quakes
