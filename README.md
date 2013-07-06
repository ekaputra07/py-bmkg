py-bmkg
=======

A Python wrapper for accessing earth quake, climate data in Indonesia based on BMKG (http://data.bmkg.go.id/).

This is new project, new wrapper will be added gradually. For now it includes:

1. **Earth Quake data fetcher.**

    Earth quake data fetcher, fetch latest (single or multi) of earth quakes that officially recorded by BMKG.

    Usage example:
    
        from bmkg.quake import Quake
        
        q = Quake()
        
        # All recently detected Quakes
        print '--------------- Recently Earth Quake ------------------'
        quakes = q.latest_quakes()
        print quakes
        
        # Latest Quakes (single)
        print '--------------- Latest Earth Quake ------------------'
        quakes = q.latest_quakes(single=True)
        print quakes
    

I hope I can add more and more tools soon.