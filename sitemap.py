from datetime import datetime
from os.path import join, getmtime

HEAD="""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">"""

TAIL="""</urlset>"""

BODY="""<url>
	<loc>{url}</loc>
	<lastmod>{lastmod}</lastmod>
</url>"""

BASE_DIR="_site"
FILES="""articles/index.html
books/index.html
coaching/index.html
index.html
leadership/index.html
tecniche/index.html
training/index.html
webinars/index.html"""

BASE_URL="http://www.luisaferrario.com/"

if __name__ == '__main__':
	with open( 'sitemap.xml', 'w' ) as f:
		f.write( HEAD + '\n' )
		for path in FILES.splitlines():
			abspath = join( BASE_DIR, path )
			lastmod = datetime.fromtimestamp( getmtime( abspath ) ).isoformat()
			url = BASE_URL + path
			f.write( BODY.format( url = url , lastmod = lastmod ) + '\n' )
		f.write( TAIL + '\n' )
