import os
import sys

sys.path.append("./data")
sys.path.append(".")

def deploy_to_server(appname):
    os.system("mkdir -p testserver/testserver/static/css")
    os.system("mkdir -p testserver/testserver/static/js")
    os.system("mkdir -p testserver/testserver/static/images")
    os.system("mkdir -p testserver/testserver/templates")
    os.system("cp  tersity/genapps/%s/css/* testserver/testserver/static/css/" % appname)
    os.system("cp  tersity/genapps/%s/js/* testserver/testserver/static/js/" % appname)
    os.system("cp  tersity/genapps/%s/images/* testserver/testserver/static/images/" % appname)
    os.system("cp  tersity/genapps/%s/templates/* testserver/testserver/templates" % appname)

def run_tersity(clean=False, inputfile=None):
    if clean:
        clean_tersity()
    currdir = os.getcwd()
    os.chdir("./tersity")
    os.system("python tersity_runner.py %s" % inputfile)
    os.chdir(currdir)


def clean_tersity():
    os.system("rm -rf tersity/genapps/*")


def usage():
    print "python run.py <inputfile> [appname]"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    run_tersity(clean=True, inputfile=sys.argv[1])
    if len(sys.argv) > 2:
        deploy_to_server(appname=sys.argv[2])
