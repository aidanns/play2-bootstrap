package controllers;

import play.*;
import play.mvc.*;

import views.html.*;

public class Application extends Controller {
  
  public static Result index() {
    return ok(main.render("Bootstrap Java Sample", index.render("Bootstrapped!")));
  }
  
}