from core import Function

# @todo ability to provide code snippets via a separate file (using a new property such as codefile)
onlogin = Function(name="on_login", code="""
$scope.on_login = function() {
    console.log("on_login: the real deal");
    LoginAPI.login("a", "b");

}

""")