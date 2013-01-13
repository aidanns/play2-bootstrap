#! /usr/bin/env python

# Moves all the required files from the bootstrap git repo to the place where they are needed for play to compile them.
# Run it from the root of the module play application.

import fileinput
import os
import shutil

# Constants
bootstrap_relative_path = "lib/bootstrap"
assets_relative_path = "app/assets"
public_relative_path = "public"

bootstrap_less_relative_path = os.path.join(bootstrap_relative_path, "less")
assets_less_relative_path = os.path.join(assets_relative_path, "stylesheets")

bootstrap_javascript_relative_path = os.path.join(bootstrap_relative_path, "js")
assets_javascript_relative_path = os.path.join(assets_relative_path, "javascripts")

bootstrap_image_relative_path = os.path.join(bootstrap_relative_path, "img")
public_images_relative_path = os.path.join(public_relative_path, "images")


def move_styles():
    # Move all the less files in to the assets directory from which they can be compiled.
    for file in os.listdir(bootstrap_less_relative_path):
        if file.endswith(".less"):
            shutil.copyfile(os.path.join(bootstrap_less_relative_path, file), os.path.join(assets_less_relative_path, file))
    # Make the name of the responsive css file the same as in the docs.
    shutil.move(os.path.join(assets_less_relative_path, "responsive.less"), os.path.join(assets_less_relative_path, "bootstrap-responsive.less"))
    # Change the directory for the images used in the stylesheet
    for line in fileinput.input(os.path.join(assets_less_relative_path, "variables.less"), inplace=1):
        if line.startswith("@iconSpritePath"):
            print "@iconSpritePath:          \"../images/glyphicons-halflings.png\";"
        elif line.startswith("@iconWhiteSpritePath"):
            print "@iconWhiteSpritePath:     \"../images/glyphicons-halflings-white.png\";"
        else:
            print "%s" % line,
    return


def move_images():
    # Move the image files in to the public directory so they will get served.
    for file in os.listdir(bootstrap_image_relative_path):
        shutil.copyfile(os.path.join(bootstrap_image_relative_path, file), os.path.join(public_images_relative_path, file))
    return


def move_javascripts():
    # Move all the javascripts in to the assets directory from which they can be compiled.
    for file in os.listdir(bootstrap_javascript_relative_path):
        if file.endswith(".js"):
            shutil.copyfile(os.path.join(bootstrap_javascript_relative_path, file), os.path.join(assets_javascript_relative_path, file))
    return

if __name__ == "__main__":
    move_styles()
    move_images()
    move_javascripts()
