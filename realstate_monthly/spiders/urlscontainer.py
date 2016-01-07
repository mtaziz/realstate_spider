#!/usr/bin/python
# -*- coding: utf-8 -*-

startURLS = [ 'https://www.realestate.com.au/neighbourhoods/Alexander%20Heights-6064-wa',
        'https://www.realestate.com.au/neighbourhoods/Alfred%20Cove-6154-wa',
        'https://www.realestate.com.au/neighbourhoods/Alkimos-6038-wa',
        'https://www.realestate.com.au/neighbourhoods/Anketell-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/Applecross-6153-wa',
        'https://www.realestate.com.au/neighbourhoods/Ardross-6153-wa',
        'https://www.realestate.com.au/neighbourhoods/Armadale-6112-wa',
        'https://www.realestate.com.au/neighbourhoods/Ascot-6104-wa',
        'https://www.realestate.com.au/neighbourhoods/Ashby-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Ashfield-6054-wa',
        'https://www.realestate.com.au/neighbourhoods/Attadale-6156-wa',
        'https://www.realestate.com.au/neighbourhoods/Atwell-6164-wa',
        'https://www.realestate.com.au/neighbourhoods/Aubin%20Grove-6164-wa',
        'https://www.realestate.com.au/neighbourhoods/Australind-6233-wa',
        'https://www.realestate.com.au/neighbourhoods/Balcatta-6021-wa',
        'https://www.realestate.com.au/neighbourhoods/Baldivis-6171-wa',
        'https://www.realestate.com.au/neighbourhoods/Balga-6061-wa',
        'https://www.realestate.com.au/neighbourhoods/Ballajura-6066-wa',
        'https://www.realestate.com.au/neighbourhoods/Banjup-6164-wa',
        'https://www.realestate.com.au/neighbourhoods/Banksia%20Grove-6031-wa',
        'https://www.realestate.com.au/neighbourhoods/Banksiadale-6213-wa',
        'https://www.realestate.com.au/neighbourhoods/Barragup-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Baskerville-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Bassendean-6054-wa',
        'https://www.realestate.com.au/neighbourhoods/Bateman-6150-wa',
        'https://www.realestate.com.au/neighbourhoods/Bayswater-6053-wa',
        'https://www.realestate.com.au/neighbourhoods/Beaconsfield-6162-wa',
        'https://www.realestate.com.au/neighbourhoods/Beckenham-6107-wa',
        'https://www.realestate.com.au/neighbourhoods/Bedford-6052-wa',
        'https://www.realestate.com.au/neighbourhoods/Bedfordale-6112-wa',
        'https://www.realestate.com.au/neighbourhoods/Beechboro-6063-wa',
        'https://www.realestate.com.au/neighbourhoods/Beeliar-6164-wa',
        'https://www.realestate.com.au/neighbourhoods/Beldon-6027-wa',
        'https://www.realestate.com.au/neighbourhoods/Belhus-6069-wa',
        'https://www.realestate.com.au/neighbourhoods/Bellevue-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Belmont-6104-wa',
        'https://www.realestate.com.au/neighbourhoods/Bentley-6102-wa',
        'https://www.realestate.com.au/neighbourhoods/Bertram-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/Bibra%20Lake-6163-wa',
        'https://www.realestate.com.au/neighbourhoods/Bickley-6076-wa',
        'https://www.realestate.com.au/neighbourhoods/Bicton-6157-wa',
        'https://www.realestate.com.au/neighbourhoods/Binningup-6233-wa',
        'https://www.realestate.com.au/neighbourhoods/Birchmont-6214-wa',
        'https://www.realestate.com.au/neighbourhoods/Blythewood-6208-wa',
        'https://www.realestate.com.au/neighbourhoods/Booragoon-6154-wa',
        'https://www.realestate.com.au/neighbourhoods/Bouvard-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Boya-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Brentwood-6153-wa',
        'https://www.realestate.com.au/neighbourhoods/Breton%20Bay-6043-wa',
        'https://www.realestate.com.au/neighbourhoods/Brigadoon-6069-wa',
        'https://www.realestate.com.au/neighbourhoods/Broadway%20Nedlands-6009-wa',
        'https://www.realestate.com.au/neighbourhoods/Brookdale-6112-wa',
        'https://www.realestate.com.au/neighbourhoods/Bull%20Creek-6149-wa',
        'https://www.realestate.com.au/neighbourhoods/Bullsbrook-6084-wa',
        'https://www.realestate.com.au/neighbourhoods/Bunbury-6230-wa',
        'https://www.realestate.com.au/neighbourhoods/Bunbury-6231-wa',
        'https://www.realestate.com.au/neighbourhoods/Burns%20Beach-6028-wa',
        'https://www.realestate.com.au/neighbourhoods/Burswood-6100-wa',
        'https://www.realestate.com.au/neighbourhoods/Butler-6036-wa',
        'https://www.realestate.com.au/neighbourhoods/Byford-6122-wa',
        'https://www.realestate.com.au/neighbourhoods/Calista-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/Canning%20Bridge%20Applecross-6153-wa',
        'https://www.realestate.com.au/neighbourhoods/Canning%20Mills-6111-wa',
        'https://www.realestate.com.au/neighbourhoods/Canning%20Vale-6155-wa',
        'https://www.realestate.com.au/neighbourhoods/Canning%20Vale%20South-6155-wa',
        'https://www.realestate.com.au/neighbourhoods/Cannington-6107-wa',
        'https://www.realestate.com.au/neighbourhoods/Caraban-6041-wa',
        'https://www.realestate.com.au/neighbourhoods/Carabooda-6033-wa',
        'https://www.realestate.com.au/neighbourhoods/Cardup-6122-wa',
        'https://www.realestate.com.au/neighbourhoods/Carey%20Park-6230-wa',
        'https://www.realestate.com.au/neighbourhoods/Carine-6020-wa',
        'https://www.realestate.com.au/neighbourhoods/Carlisle-6101-wa',
        'https://www.realestate.com.au/neighbourhoods/Carmel-6076-wa',
        'https://www.realestate.com.au/neighbourhoods/Carramar-6031-wa',
        'https://www.realestate.com.au/neighbourhoods/Casuarina-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/Caversham-6055-wa',
        'https://www.realestate.com.au/neighbourhoods/Champion%20Lakes-6111-wa',
        'https://www.realestate.com.au/neighbourhoods/Chittering-6084-wa',
        'https://www.realestate.com.au/neighbourhoods/Churchlands-6018-wa',
        'https://www.realestate.com.au/neighbourhoods/City%20Beach-6015-wa',
        'https://www.realestate.com.au/neighbourhoods/Claremont%20North-6010-wa',
        'https://www.realestate.com.au/neighbourhoods/Claremont-6010-wa',
        'https://www.realestate.com.au/neighbourhoods/Clarkson-6030-wa',
        'https://www.realestate.com.au/neighbourhoods/Clifton-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Cloverdale-6105-wa',
        'https://www.realestate.com.au/neighbourhoods/College%20Grove-6230-wa',
        'https://www.realestate.com.au/neighbourhoods/Como-6152-wa',
        'https://www.realestate.com.au/neighbourhoods/Connolly-6027-wa',
        'https://www.realestate.com.au/neighbourhoods/Coodanup-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Coogee-6166-wa',
        'https://www.realestate.com.au/neighbourhoods/Coolbellup-6163-wa',
        'https://www.realestate.com.au/neighbourhoods/Coolbinia-6050-wa',
        'https://www.realestate.com.au/neighbourhoods/Cooloongup-6168-wa',
        'https://www.realestate.com.au/neighbourhoods/Coolup-6214-wa',
        'https://www.realestate.com.au/neighbourhoods/Cottesloe-6011-wa',
        'https://www.realestate.com.au/neighbourhoods/Craigie-6025-wa',
        'https://www.realestate.com.au/neighbourhoods/Crawley-6009-wa',
        'https://www.realestate.com.au/neighbourhoods/Cullacabardee-6067-wa',
        'https://www.realestate.com.au/neighbourhoods/Currambine-6028-wa',
        'https://www.realestate.com.au/neighbourhoods/Daglish-6008-wa',
        'https://www.realestate.com.au/neighbourhoods/Dalkeith-6009-wa',
        'https://www.realestate.com.au/neighbourhoods/Dalyellup-6230-wa',
        'https://www.realestate.com.au/neighbourhoods/Darch-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Darling%20Downs-6122-wa',
        'https://www.realestate.com.au/neighbourhoods/Darlington-6070-wa',
        'https://www.realestate.com.au/neighbourhoods/Davenport-6230-wa',
        'https://www.realestate.com.au/neighbourhoods/Dawesville-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Dianella-6059-wa',
        'https://www.realestate.com.au/neighbourhoods/Dog%20Swamp-6060-wa',
        'https://www.realestate.com.au/neighbourhoods/Doubleview-6018-wa',
        'https://www.realestate.com.au/neighbourhoods/Dudley%20Park-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Duncraig-6023-wa',
        'https://www.realestate.com.au/neighbourhoods/Dwellingup-6213-wa',
        'https://www.realestate.com.au/neighbourhoods/East%20Bunbury-6230-wa',
        'https://www.realestate.com.au/neighbourhoods/East%20Fremantle-6158-wa',
        'https://www.realestate.com.au/neighbourhoods/East%20Perth-6004-wa',
        'https://www.realestate.com.au/neighbourhoods/East%20Rockingham-6168-wa',
        'https://www.realestate.com.au/neighbourhoods/East%20Victoria%20Park-6101-wa',
        'https://www.realestate.com.au/neighbourhoods/Eaton-6232-wa',
        'https://www.realestate.com.au/neighbourhoods/Eden%20Hill-6054-wa',
        'https://www.realestate.com.au/neighbourhoods/Edgewater-6027-wa',
        'https://www.realestate.com.au/neighbourhoods/Eglinton-6034-wa',
        'https://www.realestate.com.au/neighbourhoods/Ellenbrook%20East-6069-wa',
        'https://www.realestate.com.au/neighbourhoods/Ellenbrook-6069-wa',
        'https://www.realestate.com.au/neighbourhoods/Embleton-6062-wa',
        'https://www.realestate.com.au/neighbourhoods/Erskine-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Etmilyn-6213-wa',
        'https://www.realestate.com.au/neighbourhoods/Fairbridge-6208-wa',
        'https://www.realestate.com.au/neighbourhoods/Falcon-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Ferndale-6148-wa',
        'https://www.realestate.com.au/neighbourhoods/Floreat-6014-wa',
        'https://www.realestate.com.au/neighbourhoods/Forrestdale-6112-wa',
        'https://www.realestate.com.au/neighbourhoods/Forrestfield-6058-wa',
        'https://www.realestate.com.au/neighbourhoods/Fremantle-6160-wa',
        'https://www.realestate.com.au/neighbourhoods/Furnissdale-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Gabbadah-6041-wa',
        'https://www.realestate.com.au/neighbourhoods/Garden%20Island-6168-wa',
        'https://www.realestate.com.au/neighbourhoods/Gelorup-6230-wa',
        'https://www.realestate.com.au/neighbourhoods/Gidgegannup-6083-wa',
        'https://www.realestate.com.au/neighbourhoods/Girrawheen-6064-wa',
        'https://www.realestate.com.au/neighbourhoods/Glen%20Forrest-6071-wa',
        'https://www.realestate.com.au/neighbourhoods/Glen%20Iris-6230-wa',
        'https://www.realestate.com.au/neighbourhoods/Glendalough-6016-wa',
        'https://www.realestate.com.au/neighbourhoods/Glengarry-6023-wa',
        'https://www.realestate.com.au/neighbourhoods/Gnangara-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Golden%20Bay-6174-wa',
        'https://www.realestate.com.au/neighbourhoods/Gooseberry%20Hill-6076-wa',
        'https://www.realestate.com.au/neighbourhoods/Gosnells-6110-wa',
        'https://www.realestate.com.au/neighbourhoods/Greenfields-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Greenmount-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Greenwood-6024-wa',
        'https://www.realestate.com.au/neighbourhoods/Guilderton-6041-wa',
        'https://www.realestate.com.au/neighbourhoods/Guildford-6055-wa',
        'https://www.realestate.com.au/neighbourhoods/Gwelup-6018-wa',
        'https://www.realestate.com.au/neighbourhoods/Hacketts%20Gully-6076-wa',
        'https://www.realestate.com.au/neighbourhoods/Halls%20Head-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Hamersley-6022-wa',
        'https://www.realestate.com.au/neighbourhoods/Hamilton%20Hill-6163-wa',
        'https://www.realestate.com.au/neighbourhoods/Hammond%20Park-6164-wa',
        'https://www.realestate.com.au/neighbourhoods/Hazelmere-6055-wa',
        'https://www.realestate.com.au/neighbourhoods/Heathridge-6027-wa',
        'https://www.realestate.com.au/neighbourhoods/Helena%20Valley-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Henderson-6166-wa',
        'https://www.realestate.com.au/neighbourhoods/Henley%20Brook-6055-wa',
        'https://www.realestate.com.au/neighbourhoods/Herne%20Hill-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Herron-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/High%20Wycombe-6057-wa',
        'https://www.realestate.com.au/neighbourhoods/Highgate-6003-wa',
        'https://www.realestate.com.au/neighbourhoods/Hillarys-6025-wa',
        'https://www.realestate.com.au/neighbourhoods/Hillman-6168-wa',
        'https://www.realestate.com.au/neighbourhoods/Hilton-6163-wa',
        'https://www.realestate.com.au/neighbourhoods/Hocking-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Holyoake-6213-wa',
        'https://www.realestate.com.au/neighbourhoods/Hope%20Valley-6165-wa',
        'https://www.realestate.com.au/neighbourhoods/Hopeland-6125-wa',
        'https://www.realestate.com.au/neighbourhoods/Hovea-6071-wa',
        'https://www.realestate.com.au/neighbourhoods/Huntingdale-6110-wa',
        'https://www.realestate.com.au/neighbourhoods/Iluka-6028-wa',
        'https://www.realestate.com.au/neighbourhoods/Inglehope-6213-wa',
        'https://www.realestate.com.au/neighbourhoods/Inglewood-6052-wa',
        'https://www.realestate.com.au/neighbourhoods/Innaloo-6018-wa',
        'https://www.realestate.com.au/neighbourhoods/Jandabup-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Jandakot-6164-wa',
        'https://www.realestate.com.au/neighbourhoods/Jane%20Brook-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Jarrahdale-6124-wa',
        'https://www.realestate.com.au/neighbourhoods/Jindalee-6036-wa',
        'https://www.realestate.com.au/neighbourhoods/Jolimont-6014-wa',
        'https://www.realestate.com.au/neighbourhoods/Joondalup-6027-wa',
        'https://www.realestate.com.au/neighbourhoods/Joondanna-6060-wa',
        'https://www.realestate.com.au/neighbourhoods/Kalamunda-6076-wa',
        'https://www.realestate.com.au/neighbourhoods/Kallaroo-6025-wa',
        'https://www.realestate.com.au/neighbourhoods/Karakin-6044-wa',
        'https://www.realestate.com.au/neighbourhoods/Karawara-6152-wa',
        'https://www.realestate.com.au/neighbourhoods/Kardinya-6163-wa',
        'https://www.realestate.com.au/neighbourhoods/Karnup-6176-wa',
        'https://www.realestate.com.au/neighbourhoods/Karragullen-6111-wa',
        'https://www.realestate.com.au/neighbourhoods/Karrakatta-6010-wa',
        'https://www.realestate.com.au/neighbourhoods/Karrakup-6122-wa',
        'https://www.realestate.com.au/neighbourhoods/Karrinyup-6018-wa',
        'https://www.realestate.com.au/neighbourhoods/Kelmscott-6111-wa',
        'https://www.realestate.com.au/neighbourhoods/Kensington-6151-wa',
        'https://www.realestate.com.au/neighbourhoods/Kenwick-6107-wa',
        'https://www.realestate.com.au/neighbourhoods/Kewdale-6105-wa',
        'https://www.realestate.com.au/neighbourhoods/Keysbrook-6126-wa',
        'https://www.realestate.com.au/neighbourhoods/Kiara-6054-wa',
        'https://www.realestate.com.au/neighbourhoods/Kings%20Park-6005-wa',
        'https://www.realestate.com.au/neighbourhoods/Kingsley-6026-wa',
        'https://www.realestate.com.au/neighbourhoods/Kingsway-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Kinross-6028-wa',
        'https://www.realestate.com.au/neighbourhoods/Koondoola-6064-wa',
        'https://www.realestate.com.au/neighbourhoods/Koongamia-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Kwinana%20Beach-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/Kwinana%20Town%20Centre-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/Lakelands-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Lancelin-6044-wa',
        'https://www.realestate.com.au/neighbourhoods/Landsdale-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Langford-6147-wa',
        'https://www.realestate.com.au/neighbourhoods/Lathlain-6100-wa',
        'https://www.realestate.com.au/neighbourhoods/Leda-6170-wa',
        'https://www.realestate.com.au/neighbourhoods/Ledge%20Point-6043-wa',
        'https://www.realestate.com.au/neighbourhoods/Leederville-6007-wa',
        'https://www.realestate.com.au/neighbourhoods/Leeming-6149-wa',
        'https://www.realestate.com.au/neighbourhoods/Leschenault-6233-wa',
        'https://www.realestate.com.au/neighbourhoods/Lesmurdie-6076-wa',
        'https://www.realestate.com.au/neighbourhoods/Lexia-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Lockridge-6054-wa',
        'https://www.realestate.com.au/neighbourhoods/Lower%20Chittering-6084-wa',
        'https://www.realestate.com.au/neighbourhoods/Lynwood-6147-wa',
        'https://www.realestate.com.au/neighbourhoods/Maddington-6109-wa',
        'https://www.realestate.com.au/neighbourhoods/Madeley-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Madora%20Bay-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Mahogany%20Creek-6072-wa',
        'https://www.realestate.com.au/neighbourhoods/Maida%20Vale-6057-wa',
        'https://www.realestate.com.au/neighbourhoods/Malaga-6090-wa',
        'https://www.realestate.com.au/neighbourhoods/Mandogalup-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/Mandurah%20East-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Mandurah%20North-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Mandurah-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Manning-6152-wa',
        'https://www.realestate.com.au/neighbourhoods/Marangaroo-6064-wa',
        'https://www.realestate.com.au/neighbourhoods/Mardella-6125-wa',
        'https://www.realestate.com.au/neighbourhoods/Mariginiup-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Marmion-6020-wa',
        'https://www.realestate.com.au/neighbourhoods/Marrinup-6213-wa',
        'https://www.realestate.com.au/neighbourhoods/Martin-6110-wa',
        'https://www.realestate.com.au/neighbourhoods/Maylands-6051-wa',
        'https://www.realestate.com.au/neighbourhoods/Meadow%20Springs-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Medina-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/Meelon-6208-wa',
        'https://www.realestate.com.au/neighbourhoods/Melaleuca-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Melville-6156-wa',
        'https://www.realestate.com.au/neighbourhoods/Menora-6050-wa',
        'https://www.realestate.com.au/neighbourhoods/Merriwa-6030-wa',
        'https://www.realestate.com.au/neighbourhoods/Middle%20Swan-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Midland-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Midvale-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Millbridge-6232-wa',
        'https://www.realestate.com.au/neighbourhoods/Millendon-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Mindarie-6030-wa',
        'https://www.realestate.com.au/neighbourhoods/Mirrabooka-6061-wa',
        'https://www.realestate.com.au/neighbourhoods/Morangup-6083-wa',
        'https://www.realestate.com.au/neighbourhoods/Morley-6062-wa',
        'https://www.realestate.com.au/neighbourhoods/Mosman%20Park-6012-wa',
        'https://www.realestate.com.au/neighbourhoods/Mount%20Claremont-6010-wa',
        'https://www.realestate.com.au/neighbourhoods/Mount%20Hawthorn-6016-wa',
        'https://www.realestate.com.au/neighbourhoods/Mount%20Helena-6082-wa',
        'https://www.realestate.com.au/neighbourhoods/Mount%20Lawley-6050-wa',
        'https://www.realestate.com.au/neighbourhoods/Mount%20Nasura-6112-wa',
        'https://www.realestate.com.au/neighbourhoods/Mount%20Pleasant-6153-wa',
        'https://www.realestate.com.au/neighbourhoods/Mount%20Richon-6112-wa',
        'https://www.realestate.com.au/neighbourhoods/Mullaloo-6027-wa',
        'https://www.realestate.com.au/neighbourhoods/Mundaring-6073-wa',
        'https://www.realestate.com.au/neighbourhoods/Mundijong-6123-wa',
        'https://www.realestate.com.au/neighbourhoods/Munster-6166-wa',
        'https://www.realestate.com.au/neighbourhoods/Murdoch-6150-wa',
        'https://www.realestate.com.au/neighbourhoods/Myara-6207-wa',
        'https://www.realestate.com.au/neighbourhoods/Myaree-6154-wa',
        'https://www.realestate.com.au/neighbourhoods/Nambeelup-6207-wa',
        'https://www.realestate.com.au/neighbourhoods/Naval%20Base-6165-wa',
        'https://www.realestate.com.au/neighbourhoods/Nedlands-6009-wa',
        'https://www.realestate.com.au/neighbourhoods/Neerabup-6031-wa',
        'https://www.realestate.com.au/neighbourhoods/Nilgen-6044-wa',
        'https://www.realestate.com.au/neighbourhoods/Nirimba-6208-wa',
        'https://www.realestate.com.au/neighbourhoods/Nollamara-6061-wa',
        'https://www.realestate.com.au/neighbourhoods/Noranda-6062-wa',
        'https://www.realestate.com.au/neighbourhoods/North%20Beach-6020-wa',
        'https://www.realestate.com.au/neighbourhoods/North%20Dandalup-6207-wa',
        'https://www.realestate.com.au/neighbourhoods/North%20Fremantle-6159-wa',
        'https://www.realestate.com.au/neighbourhoods/North%20Lake-6163-wa',
        'https://www.realestate.com.au/neighbourhoods/North%20Perth-6006-wa',
        'https://www.realestate.com.au/neighbourhoods/North%20Yunderup-6208-wa',
        'https://www.realestate.com.au/neighbourhoods/Northbridge-6003-wa',
        'https://www.realestate.com.au/neighbourhoods/Nowergup-6032-wa',
        'https://www.realestate.com.au/neighbourhoods/Oconnor-6163-wa',
        'https://www.realestate.com.au/neighbourhoods/Oakford-6121-wa',
        'https://www.realestate.com.au/neighbourhoods/Oakley-6208-wa',
        'https://www.realestate.com.au/neighbourhoods/Ocean%20Reef-6027-wa',
        'https://www.realestate.com.au/neighbourhoods/Oldbury-6121-wa',
        'https://www.realestate.com.au/neighbourhoods/Orange%20Grove-6109-wa',
        'https://www.realestate.com.au/neighbourhoods/Orelia-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/Osborne%20Park-6017-wa',
        'https://www.realestate.com.au/neighbourhoods/Padbury-6025-wa',
        'https://www.realestate.com.au/neighbourhoods/Palmyra-6157-wa',
        'https://www.realestate.com.au/neighbourhoods/Parkerville-6081-wa',
        'https://www.realestate.com.au/neighbourhoods/Parkfield-6233-wa',
        'https://www.realestate.com.au/neighbourhoods/Parklands-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Parkwood-6147-wa',
        'https://www.realestate.com.au/neighbourhoods/Parmelia-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/Paulls%20Valley-6076-wa',
        'https://www.realestate.com.au/neighbourhoods/Pearsall-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Pelican%20Point-6230-wa',
        'https://www.realestate.com.au/neighbourhoods/Peppermint%20Grove-6011-wa',
        'https://www.realestate.com.au/neighbourhoods/Peron-6168-wa',
        'https://www.realestate.com.au/neighbourhoods/Perth%20Airport-6105-wa',
        'https://www.realestate.com.au/neighbourhoods/Perth-6000-wa',
        'https://www.realestate.com.au/neighbourhoods/Pickering%20Brook-6076-wa',
        'https://www.realestate.com.au/neighbourhoods/Piesse%20Brook-6076-wa',
        'https://www.realestate.com.au/neighbourhoods/Pinjar-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Pinjarra-6208-wa',
        'https://www.realestate.com.au/neighbourhoods/Point%20Grey-6208-wa',
        'https://www.realestate.com.au/neighbourhoods/Port%20Kennedy-6172-wa',
        'https://www.realestate.com.au/neighbourhoods/Postans-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/Queens%20Park-6107-wa',
        'https://www.realestate.com.au/neighbourhoods/Quinns%20Rocks-6030-wa',
        'https://www.realestate.com.au/neighbourhoods/Ravenswood-6208-wa',
        'https://www.realestate.com.au/neighbourhoods/Red%20Hill-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Redcliffe-6104-wa',
        'https://www.realestate.com.au/neighbourhoods/Reservoir-6076-wa',
        'https://www.realestate.com.au/neighbourhoods/Ridgewood-6030-wa',
        'https://www.realestate.com.au/neighbourhoods/Riverton-6148-wa',
        'https://www.realestate.com.au/neighbourhoods/Rivervale-6103-wa',
        'https://www.realestate.com.au/neighbourhoods/Rockingham-6168-wa',
        'https://www.realestate.com.au/neighbourhoods/Roleystone-6111-wa',
        'https://www.realestate.com.au/neighbourhoods/Rossmoyne-6148-wa',
        'https://www.realestate.com.au/neighbourhoods/Rottnest%20Island-6161-wa',
        'https://www.realestate.com.au/neighbourhoods/Safety%20Bay-6169-wa',
        'https://www.realestate.com.au/neighbourhoods/Salter%20Point-6152-wa',
        'https://www.realestate.com.au/neighbourhoods/Samson-6163-wa',
        'https://www.realestate.com.au/neighbourhoods/San%20Remo-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Sawyers%20Valley-6074-wa',
        'https://www.realestate.com.au/neighbourhoods/Scarborough-6019-wa',
        'https://www.realestate.com.au/neighbourhoods/Seabird-6042-wa',
        'https://www.realestate.com.au/neighbourhoods/Secret%20Harbour-6173-wa',
        'https://www.realestate.com.au/neighbourhoods/Serpentine-6125-wa',
        'https://www.realestate.com.au/neighbourhoods/Seville%20Grove-6112-wa',
        'https://www.realestate.com.au/neighbourhoods/Shelley-6148-wa',
        'https://www.realestate.com.au/neighbourhoods/Shenton%20Park-6008-wa',
        'https://www.realestate.com.au/neighbourhoods/Shoalwater-6169-wa',
        'https://www.realestate.com.au/neighbourhoods/Silver%20Sands-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Sinagra-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Singleton-6175-wa',
        'https://www.realestate.com.au/neighbourhoods/Solus-6207-wa',
        'https://www.realestate.com.au/neighbourhoods/Sorrento-6020-wa',
        'https://www.realestate.com.au/neighbourhoods/South%20Bunbury-6230-wa',
        'https://www.realestate.com.au/neighbourhoods/South%20Fremantle-6162-wa',
        'https://www.realestate.com.au/neighbourhoods/South%20Guildford-6055-wa',
        'https://www.realestate.com.au/neighbourhoods/South%20Lake-6164-wa',
        'https://www.realestate.com.au/neighbourhoods/South%20Perth-6151-wa',
        'https://www.realestate.com.au/neighbourhoods/South%20Yunderup-6208-wa',
        'https://www.realestate.com.au/neighbourhoods/Southern%20River-6110-wa',
        'https://www.realestate.com.au/neighbourhoods/Spearwood-6163-wa',
        'https://www.realestate.com.au/neighbourhoods/St%20James-6102-wa',
        'https://www.realestate.com.au/neighbourhoods/Stake%20Hill-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Stirling-6021-wa',
        'https://www.realestate.com.au/neighbourhoods/Stoneville-6081-wa',
        'https://www.realestate.com.au/neighbourhoods/Stratton-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Subiaco-6008-wa',
        'https://www.realestate.com.au/neighbourhoods/Success-6164-wa',
        'https://www.realestate.com.au/neighbourhoods/Swan%20View-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Swanbourne-6010-wa',
        'https://www.realestate.com.au/neighbourhoods/Tamala%20Park-6030-wa',
        'https://www.realestate.com.au/neighbourhoods/Tapping-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Teesdale-6213-wa',
        'https://www.realestate.com.au/neighbourhoods/The%20Spectacles-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/The%20Vines-6069-wa',
        'https://www.realestate.com.au/neighbourhoods/Thornlie-6108-wa',
        'https://www.realestate.com.au/neighbourhoods/Trigg-6029-wa',
        'https://www.realestate.com.au/neighbourhoods/Tuart%20Hill-6060-wa',
        'https://www.realestate.com.au/neighbourhoods/Two%20Rocks-6037-wa',
        'https://www.realestate.com.au/neighbourhoods/Upper%20Swan-6069-wa',
        'https://www.realestate.com.au/neighbourhoods/Usher-6230-wa',
        'https://www.realestate.com.au/neighbourhoods/Victoria%20Park-6100-wa',
        'https://www.realestate.com.au/neighbourhoods/Vittoria-6230-wa',
        'https://www.realestate.com.au/neighbourhoods/Viveash-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Waikiki-6169-wa',
        'https://www.realestate.com.au/neighbourhoods/Walliston-6076-wa',
        'https://www.realestate.com.au/neighbourhoods/Wandi-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/Wangara-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Wannanup-6210-wa',
        'https://www.realestate.com.au/neighbourhoods/Wanneroo-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Warnbro-6169-wa',
        'https://www.realestate.com.au/neighbourhoods/Warwick-6024-wa',
        'https://www.realestate.com.au/neighbourhoods/Waterford-6152-wa',
        'https://www.realestate.com.au/neighbourhoods/Watermans%20Bay-6020-wa',
        'https://www.realestate.com.au/neighbourhoods/Wattle%20Grove-6107-wa',
        'https://www.realestate.com.au/neighbourhoods/Wattleup-6166-wa',
        'https://www.realestate.com.au/neighbourhoods/Wedge%20Island-6044-wa',
        'https://www.realestate.com.au/neighbourhoods/Wellard-6170-wa',
        'https://www.realestate.com.au/neighbourhoods/Wellesley-6233-wa',
        'https://www.realestate.com.au/neighbourhoods/Welshpool-6106-wa',
        'https://www.realestate.com.au/neighbourhoods/Wembley%20Downs-6019-wa',
        'https://www.realestate.com.au/neighbourhoods/Wembley-6014-wa',
        'https://www.realestate.com.au/neighbourhoods/West%20Coolup-6214-wa',
        'https://www.realestate.com.au/neighbourhoods/West%20Leederville-6007-wa',
        'https://www.realestate.com.au/neighbourhoods/West%20Perth-6005-wa',
        'https://www.realestate.com.au/neighbourhoods/West%20Pinjarra-6208-wa',
        'https://www.realestate.com.au/neighbourhoods/West%20Swan-6055-wa',
        'https://www.realestate.com.au/neighbourhoods/Westfield-6111-wa',
        'https://www.realestate.com.au/neighbourhoods/Westminster-6061-wa',
        'https://www.realestate.com.au/neighbourhoods/Whitby-6123-wa',
        'https://www.realestate.com.au/neighbourhoods/White%20Gum%20Valley-6162-wa',
        'https://www.realestate.com.au/neighbourhoods/Whiteman-6068-wa',
        'https://www.realestate.com.au/neighbourhoods/Whittaker-6207-wa',
        'https://www.realestate.com.au/neighbourhoods/Wilbinga-6041-wa',
        'https://www.realestate.com.au/neighbourhoods/Willagee-6156-wa',
        'https://www.realestate.com.au/neighbourhoods/Willetton-6155-wa',
        'https://www.realestate.com.au/neighbourhoods/Wilson-6107-wa',
        'https://www.realestate.com.au/neighbourhoods/Winthrop-6150-wa',
        'https://www.realestate.com.au/neighbourhoods/Withers-6230-wa',
        'https://www.realestate.com.au/neighbourhoods/Woodbridge-6056-wa',
        'https://www.realestate.com.au/neighbourhoods/Woodlands-6018-wa',
        'https://www.realestate.com.au/neighbourhoods/Woodridge-6041-wa',
        'https://www.realestate.com.au/neighbourhoods/Woodvale-6026-wa',
        'https://www.realestate.com.au/neighbourhoods/Wungong-6112-wa',
        'https://www.realestate.com.au/neighbourhoods/Yanchep-6035-wa',
        'https://www.realestate.com.au/neighbourhoods/Yangebup-6164-wa',
        'https://www.realestate.com.au/neighbourhoods/Yokine-6060-wa',
        'https://www.realestate.com.au/neighbourhoods/Alkimos-6038-wa',
        'https://www.realestate.com.au/neighbourhoods/Anketell-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/East%20Perth-6004-wa',
        'https://www.realestate.com.au/neighbourhoods/Applecross-6153-wa',
        'https://www.realestate.com.au/neighbourhoods/Ardross-6153-wa',
        'https://www.realestate.com.au/neighbourhoods/Armadale-6112-wa',
        'https://www.realestate.com.au/neighbourhoods/Ashby-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Ascot-6104-wa',
        ]

def getStartURLS():
	return startURLS