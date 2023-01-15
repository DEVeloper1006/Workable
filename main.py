def func(city, province):
    print(city,province)
    import tkinter as tk
    import tkintermapview
    import webbrowser
    import requests
    from bs4 import BeautifulSoup
    import Homepage

    global currentPrice
    global currentAddress

    def findHousing(city, province):
        url = f"https://www.remax.ca/{province}/{city}-real-estate?pageNumber=1"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        result = [url]
        for item in soup.select(".listing-card_root__UG576") :
            result.append({"Price": item.select("[class=listing-card_price__sL9TT]")[0].get_text(), "Address" : item.select("[data-cy=property-address]")[0].get_text()})
        return result

    def findJob(city):
        url = f"https://www.bing.com/jobs?q=jobs+near+{city}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        result = [url]
        for item in soup.select(".jb_jlc") :
            result.append(item.select(".jbovrly_title")[0].get_text())
        return result

    def create_marker(address):
        print(address)
        lat,lng = tkintermapview.convert_address_to_coordinates(address)
        print(lat,lng)
        map_widget.set_marker(lat,lng)

    def next_page():
        global counter
        counter += 1
        currentPrice = housing[counter]['Price']
        currentAddress = housing[counter]['Address']
        H_PriceText.configure(text="Price: " + currentPrice)
        H_AddressText.configure(text="Address: " + currentAddress)
        map_widget.set_address(currentAddress)
        map_widget.set_zoom(11)
        create_marker(currentAddress)
        jobs = findJob('Waterloo')

    def prev_page():
        global counter
        counter -=1
        currentPrice = housing[counter]['Price']
        currentAddress = housing[counter]['Address']
        H_PriceText.configure(text=currentPrice)
        H_AddressText.configure(text=currentAddress)
        map_widget.set_address(currentAddress)
        map_widget.set_zoom(11)
        create_marker(currentAddress)

    def goToLink(link):
        webbrowser.open_new(link)

    housing = findHousing(city,province)
    remaxUrl = housing[0]
    housing = housing[1:]

    counter=0
    currentPrice = housing[counter]['Price']
    currentAddress = housing[counter]['Address']

    jobs = findJob(city)
    bingUrl = jobs[0]
    jobs = jobs[1:]

    root = tk.Tk()
    root.title('Page - MapView')
    root.geometry("800x600")




    myMap = tk.Label(root)

    map_widget = tkintermapview.TkinterMapView(myMap, width=700, height=350)

    # set coordinates
    map_widget.set_address(currentAddress)
    map_widget.set_zoom(11)


    create_marker(currentAddress)


    # List View
    myMap.pack(padx=0)
    map_widget.pack(pady=10)

    # Housing
    HouseHeader = tk.Label(root,text="Housing",font=("Futura",18))
    HouseHeader.place(x=50,y=375)

    H_PriceText = tk.Label(root,text="Price: "+currentPrice, font=("Futura",14))
    H_PriceText.place(x=50,y=405)

    H_AddressText = tk.Label(root,text="Address: "+currentAddress,font=("Futura",14))
    H_AddressText.place(x=50,y=430)

    goToRemax = tk.Button(root, text="View Listings", command= lambda:goToLink(remaxUrl))
    goToRemax.place(x=50,y=550)

    # Nearby
    NearbyHeader = tk.Label(root,text="Nearby",font=("Futura",18))
    NearbyHeader.place(x=375,y=375)

    goToGrocery = tk.Button(root, text="Nearby Groceries", command= lambda: goToLink("https://google.com/maps/search/Groceries/{}".format(currentAddress)))
    goToGrocery.place(x=360,y=430)

    goToRestaurants = tk.Button(root, text="Nearby Restaurants", command= lambda: goToLink("https://google.com/maps/search/Restaurants/{}".format(currentAddress)))
    goToRestaurants.place(x=360,y=470)

    goToRecreation = tk.Button(root, text="Nearby Recreation", command= lambda: goToLink("https://google.com/maps/search/Recreation/{}".format(currentAddress)))
    goToRecreation.place(x=360,y=510)

    goToReligous = tk.Button(root, text="Nearby Religious Places", command= lambda: goToLink("https://google.com/maps/search/Religous+Places/{}".format(currentAddress)))
    goToReligous.place(x=360,y=550)

    # Work

    JobHeader = tk.Label(root,text="Suggested Work",font=("Futura",18))
    JobHeader.place(x=595,y=375)

    J_Title1 = tk.Label(root,text="Job Title: "+jobs[0],font=("Futura",14))
    J_Title1.place(x=580,y=405)

    J_Title2 = tk.Label(root,text="Job Title: "+jobs[1],font=("Futura",14))
    J_Title2.place(x=580,y=435)

    J_Title3 = tk.Label(root,text="Job Title: "+jobs[2],font=("Futura",14))
    J_Title3.place(x=580,y=465)


    goToIndeed = tk.Button(root, text="View More", command = lambda: goToLink("https://indeed.ca"))
    goToIndeed.place(x=650,y=550)

    next = tk.Button(root, text="Next", command=next_page)
    next.place(x=550,y=550)

    back = tk.Button(root, text="Back", command=prev_page)
    back.place(x=300,y=550)

    root.mainloop()
