import requests

class CanvasApi:
    def __init__(self):
        self.__baseUrl = 'http://www.canvas.be/api/video/'

        #Categories for filtering
        self.categories = dict([
            ('Music','vd352'),
            ('Science','vd320'),
            ('Bizz','vd321'),
            ('Culture','vd256'),
            ('Literature','vd1080'),
            ('Sports','vd323'),
            ('Only online','vd258'),
            ('Politics','vd657'),
            ('Society','vd518')])

        #Sorting options for the api
        self.sorting = dict([
            ('Recent','-date'),
            ('Oldest','date'),
            ('Expiring','expiring'),
            ('Shortest','length'),
            ('Longest', '-length')])

    def _build_url(self,page ,sorting, *categories):
        """Create the api url
        Get a specific page
        In a specif order
        For some categories (No categories defined = returns everything)
        """
        url = self.__baseUrl + str(page) + '/0,999999/'+ str(sorting) + '/'

        if categories:
            #add the categories to the url
            #Should be a sorted list, otherwise doesn't work
            cat = ''
            for c in sorted(categories):
                cat += str(c) + ','

            #Trim last comma
            cat = cat[:-1]
            #Always end with /
            url += cat + '/'

        return url


    def recent(self, page, *categories):
        """Get the recently added content"""
        url = self._build_url(page, self.sorting['Recent'], categories)
        r = requests.get(url)
        return r.json()

    def expiring(self, page, *categories):
        """Get the content that will be unavailable soon."""
        url = self._build_url(page, self.sorting['Expiring'], categories)
        r = requests.get(url)
        return r.json()
