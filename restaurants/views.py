from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list" : [
    		{
    			"restaurant_name": "Burger King" ,
    			"food_type": "Fast Food" 
    		},
    		{
    			"restaurant_name": "Pizza Hut" ,
    			"food_type": "Italian"
    		},
    		{
    			"restaurant_name": "Villa Firuze" ,
    			"food_type": "Libanese" 
    		}
    	]
    }

    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object" : {
    		"restaurant_name" : "Villa Firuze",
    		"food_type" : "Libanese"
    	}

    }
    return render(request, 'detail.html', context)
