# TODO: Generate random search strings
	# Initally unif. random from a dictionary, of random length (1-5 words).
	# In future, create a simple markov chain monte carlo to do this.
# TODO: Generalize user-agent to whatever the user has on the computer.
# TODO: Incorporate timing mechanism.
# TODO: Chose a random number of links (between 1 and 3) and follow them.
# TODO: Link browser history to noisemaker history.
# TODO: Read through more documentation on python, mechanize, and cookielib.
# TODO: Pick better variable names than currently have.

import mechanize
import cookielib

# Browser
browse = mechanize.Browser()

# Dig into what these lines do. Clearly they invovle instantiating a cookie object. The characteristics of this object, however, are presently unknown.
# Cookie Jar
cj = cookielib.LWPCookieJar()
browse.set_cookiejar(cj)



# Research this 
browse.set_handle_equiv(True)


# Deals with redirects
#browse.set_handle_redirect(True)

#handles refers
#browse.set_handle_referer(True)

#ignores robots.txt
browse.set_handle_robots(False)


# 
# Follows refresh 0 but not hangs on refresh > 0
# browse.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

# user-agent  - Presently Linux. Need to figure out how to get the one for the user's browser
browse.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Accesses Google
pg = browse.open('http://google.com')
html = pg.read()

# Runs a search using the string "weekend codes"
browse.form['q']='weekend codes'
browse.submit()

searchResult=browse.response().read()


