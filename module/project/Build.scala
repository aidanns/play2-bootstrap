import sbt._
import Keys._
import play.Project._

object ApplicationBuild extends Build {

    val appName         = "play2-bootstrap"
    val appVersion      = "2.2.2-SNAPSHOT"

    val appDependencies = Seq(

      javaCore, javaJdbc, javaEbean

    )

    val main = play.Project(appName, appVersion, appDependencies).settings(
      
      // Only compile the main two bootstrap
      lessEntryPoints <<= (baseDirectory in Compile) (base => (
        (base / "app" / "assets" / "stylesheets" / "bootstrap.less") +++
        (base / "app" / "assets" / "stylesheets" / "bootstrap-responsive.less")
      )),

      // Org name to use for publishing
      organization := "com.aidanns"
    )

}
