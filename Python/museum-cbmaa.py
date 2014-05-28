## Define the functions used in mapping the dataset of CBMAA
## To avoid having the same function name in different python script files, each function here adds a prefix with "cb_". 
## By Chao on 05-27-2014@ISI 


def cb_objectUri():
	return "object/" + getValue("Source Number")

def cb_objectIdentifierUri():
	return "object/" + getValue("Source Number") + "/regno"

def cb_objectTypeUri():
	return "thesauri/" + getValue("Classification").lower().replace(' ', '_')

def cb_titleUri():
	return cb_objectUri() + "/title"

def cb_seriesUri():
	val = getValue("Catalogue raisonne")
	if val:
		return "thesauri/" + val.lower().replace(' ', '_') 

# return person's URI, if person name includes 'unknown', plus the regno of the related object
def cb_creatorUri():
	personName = getValue("Maker").lower()
	if "unknown" in personName:
		return "person-institution/" + personName.replace(' ', '_') + '_' + getValue("Source Number")
	else:
		return "person-institution/" + personName.replace(' ', '_')

def cb_creatorAppellationUri():
	return cb_creatorUri() + "/appellation"

def cb_productionUri():
	return cb_objectUri() + "/production"

def cb_bibliographyUri():
	return "bibliography/" + getValue("Source Number")

def cb_publicationUri():
	return cb_bibliographyUri() + "/publication"

def cb_publicationDateUri():
	return cb_bibliographyUri() + "/publication/date"

def cb_legalBodyUri():
	if getValue("Source Name"):
		return cb_objectUri() + "/legalbody"

def cb_acquisitionUri():
	if getValue("Credit Line"):
		return cb_objectUri() + "/acquisition"

def cb_materialUri():
	val = getValue("Medium")
	if val:
		return "thesauri/material/" + val.lower().replace(" ", "_")

def cb_dimensionUri():
	val = getValue("Dimensions")
	if val:
		return cb_objectUri() + "/dimension"

def cb_inscription1Uri():
	val = getValue("Signed")
	if val:
		return cb_objectUri() + "/inscription/1"

def cb_inscription2Uri():
	val = getValue("Mark(s)")
	if val:
		return cb_objectUri() + "/inscription/2"

def cb_inscription3Uri():
	val = getValue("Inscription(s)")
	if val:
		return cb_objectUri() + "/inscription/3"