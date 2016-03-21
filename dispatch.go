package main

import (
	"fmt"
	"math"
	"time"

	"github.com/OpenBikes/gooby"
)

var city = "Toulouse"

func main() {
	// Station name
	var p0 = gooby.Current(city)
	for _, station := range p0.Features {
		var name = station.Properties.Name
		// Define the timeline
		var t0, _ = time.Parse("2006-01-02T15:04:05", station.Properties.Update)
		var t1 = t0.Add(10 * time.Minute)
		var t2 = t1.Add(60 * time.Minute)
		// Get the necessary forecasts
		var p1 = gooby.Forecast(city, name, t1.Unix())
		var p2 = gooby.Forecast(city, name, t2.Unix())
		// Number of predicted arrivals
		var arrivals = p2.Bikes.Quantity - p1.Bikes.Quantity
		var departures = p2.Stands.Quantity - p1.Stands.Quantity
		// Missing number of bikes
		var in = station.Properties.Bikes - arrivals
		var out = station.Properties.Stands - departures
		if in < 0 {
			fmt.Printf("Bring %d bike(s) to %s.\n", int(math.Abs(in)), name)
		}
		if out < 0 {
			fmt.Printf("Take %d bike(s) from %s.\n", int(math.Abs(out)), name)
		}
	}
}
