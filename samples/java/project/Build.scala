import sbt._
import Keys._
import play.Project._

object ApplicationBuild extends Build {

    val appName         = "play2-bootstrap-sample-java"
    val appVersion      = "2.2.2"

    val appDependencies = Seq(
      
   	  javaCore, javaJdbc, javaEbean,

      // We want to depend on the thing that we're demoing.
      "com.aidanns" %% "play2-bootstrap" % "2.2.2"
    
    )

    val main = play.Project(appName, appVersion, appDependencies).settings(
    
      // Search the local play repo for dependencies.
      resolvers += "Local Play Repository" at "file://usr/local/share/play-2.1-RC1/repository/",
      resolvers += Resolver.url("com.aidanns Github Repo", url("https://raw.github.com/aidanns/play2-modules/master/releases"))(Resolver.ivyStylePatterns),
    
      // Org name to use for publishing
      organization := "com.aidanns"
    )

}
