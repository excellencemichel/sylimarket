import os



def get_filename(filepath):
	base_name = os.path.basename(filepath)
	name_file, extension_file = os.path.splitext(base_name)
	return name_file, extension_file



def upload_file_location(instance, filename):
	name_product = instance.name
	id_ = instance.id
	if id_ is None:
		Klass = instance.__class__
		qs = Klass.objects.all().order_by("-pk")
		if qs.exists():
			id_ = qs.first().id + 1
		else:
			id_ = 0
	name_file, extension_file =get_filename(filename)

	final_filename = "{name_file}_{id_}{extension_file}".format(name_file=name_file, id_=id_, extension_file=extension_file)
	

	return "products/{name_product}/{final_filename}".format(name_product=name_product, final_filename=final_filename)


