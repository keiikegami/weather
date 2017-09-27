# read grib file by python2 usgin iris
import iris

# savepath include the new filename whose extension is ".pp" 
def grib_pp(filename, savepath):
    cube = iris.load(filename)
    try:
        iris.save(cube, savepath)
        return "conversion complete"
    except ValueError:
        print "unable to save the file in pp format"
        
        
# savepath include the new filename whose extension is ".grib2" 
def pp_grib(filename, savepath):
    cube = iris.load(filename)
    try:
        iris.save(cube, savepath)
        return "conversion complete"
    except ValueError:
        print "unable to save the file in GRIB format"