import json
import urllib2

base_url = 'https://secure-brook-1414.herokuapp.com'
checkout_url = base_url + '/api/checkout'
checkin_url = base_url + '/api/checkin'

def main():
    count = 0
    while 1:
        card_id = raw_input('> ')
        data = {
            'bikeID': 1,
            'dockID': 1,
            'cardString': card_id
        }
        if (count % 2) == 0:
            url = checkout_url
            print "Checkout " + card_id
        else:
            url = checkin_url
            print "Checkin " + card_id

        req = urllib2.Request(url, data=json.dumps(data))
        req.add_header('Content-Type', 'application/json')

        resp = urllib2.urlopen(req)
        count += 1

if __name__ == '__main__':
    main()
