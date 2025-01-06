from pyicloud import PyiCloudService
import os

api = PyiCloudService('stonehoo84@gmail.com')

for photo in api.photos.all:
	filename, ext = os.path.splitext(photo.filename)
	output_filename = str.format("{0}-{1}{2}", filename, photo.client_id, ext)
	if os.path.isfile(output_filename):
		print "File " + output_filename + " already exists"
		continue
	print "Writing file to " + output_filename
	download = photo.download('original');
	with open(output_filename, 'wb') as opened_file:
		opened_file.write(download.raw.read())
