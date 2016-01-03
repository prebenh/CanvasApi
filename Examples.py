import CanvasApi

if __name__ == '__main__':
    #Create instace of the api
    api = CanvasApi.CanvasApi()

    print '----------Get the most recent content------------------'
    print api.recent(1)
    print '-------Get the content that will expire soon-----------'
    print api.expiring(1)
