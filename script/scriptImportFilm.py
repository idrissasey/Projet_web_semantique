import csv
import requests


#######################################################################################################################################
############################################# PREFIXE CLASSES #########################################################################
prefixLieu           = "PREFIX LIEU:             <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_11985763_f834_40e8_8a04_414bbd5bed3d>"
prefixGenre          = "PREFIX GENRE:            <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_1ae1f291_9271_4188_bccd_456fde6439b2>"
prefixActeur         = "PREFIX GRANDACTEUR:      <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_2774958d_3ea7_4c85_ad35_f8aa12c1bff8>"
prefixFemme          = "PREFIX FEMME:            <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_307442a0_341a_4f9c_8b87_a34b48f926c9>"
prefixArtiste        = "PREFIX ARTISTE:          <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_3aac3b4b_45d9_4699_a491_5ef7adb05707>"
prefixeVille         = "PREFIX VILLE:            <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_51a5bd12_b945_4ba6_8b98_67f56a7f4a96>"
prefixeRecensement   = "PREFIX RECENSEMENT:      <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_5c0ace4a_18fa_4172_a4d7_f3317cdf79e0>"
prefixFilmEuro       = "PREFIX FILMEURO:         <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_6ff04224_070b_4c25_95b5_772526bd4501>"
prefixPays           = "PREFIX PAYS:             <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_7942daab_732a_4556_a6e4_3a4a9f23bbef>"
prefixPersonne       = "PREFIX PERSONNE:         <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_7d543f0f_5a71_448b_a058_50b72eff1bed>"
prefixMeurtre        = "PREFIX MEURTRE:          <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_950a7a16_2979_47db_b707_38d1bff008ba>"
prefixTouriste       = "PREFIX TOURISTE:         <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_a24e7b75_8d2e_48a7_b577_dafa515f6782>"
prefixNationality    = "PREFIX NATIONALITE:      <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_a6bb97d0_b045_4c0a_b125_0a4f85148161>"
prefixHomme          = "PREFIX HOMME:            <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_b17023e7_b9e3_44b2_b72d_36b9ee82e31b>"
prefixFilm           = "PREFIX FILM:             <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_b3ec988b_3df8_44bc_bb90_2242c83e3158>"
prefixAnnee          = "PREFIX ANNEE:            <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_bc3d0556_265a_4f58_b5bb_17321bc1fbf6>"
prefixContinent      = "PREFIX CONTINENT:        <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_c8ba1974_f121_4998_954d_6c0d3bd8c372>"
prefixActeurF        = "PREFIX ACTRICE:          <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_d067985f_3ce0_4e1e_8940_8fabe17d2e4d>"
prefixeLongMetrage   = "PREFIX LONGMETRAGE:      <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_dea269dd_41df_4b73_ba4f_fa9e99620933>"
prefixeActeurH       = "PREFIX ATEUR:            <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_e09aacdb_a419_4354_993b_d2c5df3e75fd>"
prefixeHabitant      = "PREFIX HABITANT:         <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_f117f070_9bde_4a82_8ad6_562b22f8a91b>"
prefixeCourtMetrage  = "PREFIX COURTMETRAGE:     <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_b3ec988b_3df8_44bc_bb90_2242c83e3158>"
prefixeRealisateur   = "PREFIX REALISATEUR:      <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#realisateur>"

#################################################################################################################################################
#################################################### PREFIXE DATA PROPERTIES ####################################################################
prefixApourAnnee     = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLDataProperty_2154ceef_5ff4_4404_b036_b6503aaeca98>"
prefixApourNombre    = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLDataProperty_4b21da79_be21_4d19_a998_022128a28404>"
prefixApourDuree     = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#aPourDuree>"
prefixApourNote      = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#aPourNote>"

#################################################################################################################################################
#################################################### PREFIXE OBJECT PROPERTIES ####################################################################
prefixSeSitueDans      = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLObjectProperty_140106e4_206f_4d61_8955_6550607692e5>"
prefixEstDeNationalite = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLObjectProperty_1d31e9ea_fdf1_4484_9cd8_a1a8e1facc53>"
prefixAJouerDans       = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLObjectProperty_3670197b_6411_4b48_928c_0bdf6431dddb>"
prefixAPourCapital     = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLObjectProperty_36bec4df_6dd2_4e0f_8c99_e0046bdbe740>"
prefixAPourActeur      = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLObjectProperty_3ea60e3f_9a49_4f58_9da2_6c283f2e1a29>"
prefixEstLaCapitalDe   = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLObjectProperty_4d8007f9_ecfe_412a_9ba7_35e2db43d035>"
prefixAPourRealisateur = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLObjectProperty_7714a382_8fbc_485a_b6b7_5ef0cc32fd41>"
prefixAPourGenre       = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLObjectProperty_77651232_45fd_4994_95e7_0e7c581fd0ac>"
prefixAccordePar       = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLObjectProperty_bd250005_48bc_4e04_bba6_6af52cc9bb6c>"
prefixAPourRecensement = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLObjectProperty_ea54c651_cd09_4455_a859_33e01977d630>"
prefixJoueAvec         = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLObjectProperty_f21cec05_5310_467e_aa0b_a84b41d2d14a>"
prefixARealise         = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#aRealise>"
prefixSeDerouleA       = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#seDerouleA>"


prefixRDFS    = "PREFIX rdfs: <http://www.w3.org/2000/01/rdfs-schema#>"
prefixRDF     = "PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>"
prefixOWL     = "PREFIX owl:  <http://www.w3.org/2002/07/owl#>"
      
compteur = 0
with open('../donnes brutes/films_paris.csv', newline='') as csvfile:
       reader = csv.DictReader(csvfile)
       for row in reader:
              requestInsertFilm           = prefixFilm + ' ' + prefixRDFS + ' INSERT DATA { FILM:film'+str(compteur) +' rdfs:label "' + row['titre'] + '"}' 
              requestInsertRealisateur    = prefixeRealisateur + ' ' + prefixRDFS + ' INSERT DATA { REALISATEUR:realisateur' + str(compteur) + ' rdfs:label "' + row['realisateur'] + '"}' 
              requestInsertARealise       = prefixARealise + ' ' + prefixFilm + ' ' + prefixeRealisateur + ' INSERT DATA { :realisateur' + str(compteur) + ' :aRealise :film' +str(compteur) + '}'       
              requestInsertAnnee          = prefixAnnee + ' ' + prefixRDFS + ' INSERT DATA { ANNEE:annee' + str(compteur) + ' rdfs:label "' + row['date_fin'] + '"}' 
              

              response = requests.post('http://localhost:3030/antology/update',
              data={'update': requestInsertFilm})
              
              reponse = requests.post('http://localhost:3030/antology/update',
              data={'update': requestInsertRealisateur})

              reponse = requests.post('http://localhost:3030/antology/update',
              data={'update': requestInsertARealise})

              reponse = requests.post('http://localhost:3030/antology/update',
              data={'update': requestInsertAnnee})

              requestInsertVile           = prefixeVille + ' ' + prefixRDFS + ' INSERT DATA { VILLE:ville' + row['ardt'] + ' rdfs:label "' + row['ardt'] + '"}' 
              requestInsertPays           = prefixPays +  ' ' + prefixRDFS + ' INSERT DATA { PAYS:france rdfs:label "France"}'   
              requestInsertSeSitueDans    = prefixPays + ' ' + prefixeVille + ' ' + prefixSeSitueDans + ' INSERT DATA { :ville' + row['ardt'] + ' :OWLObjectProperty_140106e4_206f_4d61_8955_6550607692e5 :france}'

              reponse = requests.post('http://localhost:3030/antology/update',
              data={'update': requestInsertVile})

              reponse = requests.post('http://localhost:3030/antology/update',
              data={'update': requestInsertPays})

              reponse = requests.post('http://localhost:3030/antology/update',
              data={'update': requestInsertSeSitueDans})

              compteur = compteur + 1

       print(response.json())
           



