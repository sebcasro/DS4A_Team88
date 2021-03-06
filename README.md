# DS4A - Team88

# Energy price prediction for the Colombian market using Machine Learning models.

![application home page](dash/assets/images/home_page.png)

Conexalab is an enterprise based in Bucaramanga, whose main target is to give support and guidance in the projects of their clients. On the subject of energy, they aim to promote the use of renewable energy, smart energy, energy efficiency and the reduction of carbon footprint. Another goal of Conexalab is the reduction of the social gaps through the development of different investment projects. 

## Business Problem
In order to provide a better analysis and better project proposals to its clients, Conexalab requires integrating into its studies a forecasting of the energy market price for the coming years, in order to reduce the uncertainty in the projects which involve high use of energy.

Energy price is determined by several components, such as power generation, transmission and commercialization. Under a regulatory framework supervised by *Comisión de Regulación de Energía y Gas* (CREG) ([Concepto 2180 de 2009 CREG](https://gestornormativo.creg.gov.co/gestor/entorno/docs/concepto_creg_0002180_2009.htm), [Resolución 119 de 2007 CREG](https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_0119_2007.htm#INICIO)). The generation price component represents the cost of energy purchased in the wholesale energy market. Its variation is subject to the prices of the Energy Exchange (electric energy market where all the energy necessary to supply the users connected to the National Transmission System is traded daily) and to the prices of the long-term bilateral supply contracts for the regulated market that the traders sign after advancing public calls for bids. 

It is important to highlight that this variable may present changes from one period to another, due to the fact that in Colombia the generating park is composed of both hydraulic and thermal plants for the generation of electric energy. Therefore, prices on the stock exchange, and in contracts, depend on variables such as hydrological conditions and the prices of fuels used in generation (mainly natural gas and coal).

Since the scope of this project is to be framed, after a consensus with members of Conexalab, it has been determined to carry out the analysis only on the generation component of the unit cost and especially the exchange price, for which initially the hydrological effects and the availability of power plants will be taken into account. 

## Business Impact
By creating this algorithm to forecast Kwh prices in Colombia, we will provide Conexalab a new and powerful tool to improve their calculations on the expected returns on clean energy investments. Furthermore, reducing uncertainty around future prices, Conexalab believes that projects for clean energy generation will raise more funds and will gain more participation in urban and rural areas across the country.

The dashboard we will create is meant to help Conexalab to modelate future energy prices under different assumptions, allowing them to contrast the results. We also expect this dashboard to be within their business presentation portfolio in order to improve the impact of the information they show to customers and investors.

A main and remarkable business impact we expect from this algorithm is an expansion in the number of projects of clean energy generation. Also, with the implementation of more environmentally responsible technologies we look forward to lowering our country’s carbon footprint. 
Finally, we believe that a proper construction and development of our algorithm presented in the dashboard, with significant accuracy and precision in the forecast, will increase the interest in this kind of AI tools applied to business, boosting and spreading the need for them beyond this forecasting project.

## Run the app 

All the files required to run the application locally are inside the folder *dash*. The dashboard was develop with *Python* using the library *Dash* (In order for the application to work you'll need to make sure you have installed Python in your computer).

0. (optional) We recommend you to use a virtual environment in order to prevent conflicts with other libraries you may have already installed in your computer. [A Guide to Python’s Virtual Environments](https://towardsdatascience.com/virtual-environments-104c62d48c54)

1. The first step would be to install the requirements (this file is located inside the *dash* folder), for this you can use *pip* and the following command:

```
pip install -r requirements.txt
```

2. There are two files you'll need to download (*these files were too big to be uploaded to GitHub*). Inside the *data* folder run the followings commands:

```
python descarga_datos_Disponibilidad_Real.py
```
```
python descarga_datos_Disponibilidad_Real(porcentaje).py
```

3. Once the have downloaded the files and the installation of the libraries is completed, you'll need to start the application. (inside the *dash* folder)

```
python index.py
```

4. The last step would be to access the application locally on your browser with the link:

```
http://localhost:8050/
```

## Team

This project was developed by:

* **Carlos Mario De Oro Aguado** - [LinkedIn](https://www.linkedin.com/in/cdeoroaguado/)
* **David Enrique Zambrano Higuera** - [LinkedIn](https://www.linkedin.com/in/david-enrique-zambrano-a753a764/)  - [GitHub](https://github.com/econdavidzh)
* **Jairo Andres Ruiz Saenz** - [LinkedIn](https://www.linkedin.com/in/jairoruizsaenz/)  - [GitHub](https://github.com/jairoruizsaenz)
* **Juan Sebastian Castro Rodriguez** - [LinkedIn](https://www.linkedin.com/in/juan-sebastian-castro-rodriguez-69576420b/) 
* **Pedro José Díaz Rojas** 
