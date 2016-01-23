"""
Run this script to list all meshes that are required by items but do not exist in the resources.
"""
import re
import os
import os.path
import cPickle as pickle

# , "./Brytenwalda/Resource/CrossmatchmissingfromRP/"
#res_paths = ["./Native/CommonRes/", "./Brytenwalda/Resource/"]
res_paths = ["./Native/CommonRes/", "./Brytenwalda/Resource/"]
#tex_paths = ["./Native/Textures/", "./Brytenwalda/Textures/"]


def build_resources_db():
    def read_file(path, resource_file):
        with open(path + resource_file, 'rb') as f:
            content = f.readlines()
        content = "\n".join(content)

        found = re.findall(r'\x00([a-zA-Z0-9_]{3,})[\x00\x01\.]', content)

        return found

    resources = set()
    resources_in_file = dict()
    for path in res_paths:
        for resource_file in os.listdir(path):
            if not resource_file.endswith('.brf'):
                continue

            new_resources = set(read_file(path, resource_file))

            for resource in new_resources:
                if resource not in resources_in_file:
                    resources_in_file[resource] = set()
                resources_in_file[resource].add(path + resource_file)

            resources = resources.union(new_resources)

    # for path in tex_paths:
    #     for texture_file in os.listdir(path):
    #         if not texture_file.endswith('.dds'):
    #             continue
    #         # remove .dds and add
    #         resources.add(texture_file[:-4])

    resources -= {'rfver', 'texture', 'mesh', 'manifold'}
    return resources, resources_in_file


def get_db(reload_cache=False):
    try:
        if reload_cache:
            raise IOError  # force computing the database
        with open('./temp.txt', 'r') as f:
            resources = set()
            for x in f.readlines():
                resources.add(x[:-1])

        with open('./in_files.pickle', 'r') as f:
            file_of_resource = pickle.load(f)

    except IOError:
        resources, file_of_resource = build_resources_db()
        with open('./temp.txt', 'w') as f:
            for x in sorted(resources):
                f.write("%s\n" % x)
        with open('./in_files.pickle', 'w') as f:
            pickle.dump(file_of_resource, f)

    return resources, file_of_resource


def get_used_items_meshes():
    from compiler.item import Item

    used_resources = set()
    for data in Item.raw_objects:
        item = Item(len(Item.objects), *data)

        for mesh in item.meshes:
            used_resources.add(mesh)

    return used_resources


def unused_shield_meshes(resources=None):
    if resources is None:
        resources, _ = get_db()
    used_resources = get_used_items_meshes()

    unused_shield_meshes = []
    for unused_mesh in sorted(resources - used_resources):
        for x in ['shield', 'buckler']:
            if x in unused_mesh.lower():
                unused_shield_meshes.append(unused_mesh)
    return sorted(unused_shield_meshes)


if __name__ == '__main__':

    resources, _ = get_db()
    used_resources = get_used_items_meshes()

    print('missing meshes: %d' % len(used_resources - resources))
    for x in sorted(used_resources - resources):
        print(x)

    unused_shield_meshes = unused_shield_meshes()
    print('unused shields: %d' % len(unused_shield_meshes))
    for x in unused_shield_meshes:
        print(x)
