# play2-bootstrap

A Play2 module to provide the Twitter Bootstrap assets.

Note that module runs against Play 2.1-RC1.

## What exactly does this module do?

* Provides `*.css` and `*.min.css` files within the `public\stylesheets` sub-directory of the classpath.
* Provides `*.js` and `*.min.js` files within the `public\javascripts` sub-directory of the classpath.
* Provides `*.png` files within the `public\images` sub-directory of the classpath.

Assuming you maintain the default `GET  /assets/*file controllers.Assets.at(path="/public", file)` route from the skeleton, this means all the bootstrap files will be available at `/assets/*`.

## How do I use it?

There is currently no publicly accessibly maven repo hosting the `.jar`. The easiest way to use the project is to clone the repo and build the `.jar` from within the `module` directoy. Copy the `.jar` in to the `lib` directory of your play application and you're good to go.

You can also publish the `.jar` locally and set up a dependency using SBT. See the `Build.scala` file within the sample project for an example.

## What does the repo contain?

* `module` directory contains the Play! submodule.
* `samples` directory contains a (very sparse) example of using the submodule.

## Updating the bootstrap version

This requires a working Python installation.

1. `cd module\lib\bootstrap`
2. `git pull`
3. `cd ../../`
4. `script/update.py`
5. `git add .`
6. `git commit -m "Updated to bootstrap version x.x.x"
7. Submit a pull request on Github.