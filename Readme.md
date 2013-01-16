# play2-bootstrap

A Play2 module to provide the Twitter Bootstrap assets.

Note that module runs against Play 2.1-RC1.

## What exactly does this module do?

* Provides `*.css` and `*.min.css` files within the `public\stylesheets` sub-directory of the classpath.
* Provides `*.js` and `*.min.js` files within the `public\javascripts` sub-directory of the classpath.
* Provides `*.png` files within the `public\images` sub-directory of the classpath.

Assuming you maintain the default `GET  /assets/*file controllers.Assets.at(path="/public", file)` route from the skeleton, this means all the bootstrap files will be available at `/assets/*`.

## How do I use it?

Add the following to the appDependencies section of your Build.sbt file:

`"com.aidanns" %% "play2-bootstrap" % "2.2.2"`

Add the following to the main section of your Build.sbt file:

`resolvers += Resolver.url("com.aidanns Github Repo", url("https://raw.github.com/aidanns/play2-modules/master/releases"))(Resolver.ivyStylePatterns)`

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
6. `git commit -m "Updated to bootstrap version x.x.x"`
7. Submit a pull request on Github.