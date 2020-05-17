
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Map;

public class SparqlClientExample {

	/**
	 * @param args
	 *            the command line arguments
	 */
	public static void main(String args[]) {
		SparqlClient sparqlClient = new SparqlClient("localhost:3030/film");
		System.out.println(sparqlClient);
		String query = "ASK WHERE { ?s ?p ?o }";
		boolean serverIsUp = sparqlClient.ask(query);

		if (serverIsUp) {
			System.out.println("server is UP");

			String csvFile = System.getProperty("user.home") + "\\Desktop\\population.csv";
			String line = "";
			String cvsSplitBy = ";";

			insertObject(sparqlClient, csvFile, cvsSplitBy);

			// query = "PREFIX : <http://www.lamaisondumeurtre.fr#>\n"
			// + "PREFIX instances: <http://www.lamaisondumeurtre.fr/instances#>\n" +
			// "INSERT DATA\n" + "{\n"
			// + " instances:Bob :personneDansPiece instances:Bureau.\n" + "}\n";

			// nbPersonnesParPiece(sparqlClient);
			//
			// System.out.println("suppression d'une personne du bureau:");
			// query = "PREFIX : <http://www.lamaisondumeurtre.fr#>\n"
			// + "PREFIX instances: <http://www.lamaisondumeurtre.fr/instances#>\n" +
			// "DELETE DATA\n" + "{\n"
			// + " instances:Bob :personneDansPiece instances:Bureau.\n" + "}\n";
			// sparqlClient.update(query);

		} else {
			System.out.println("service is DOWN");
		}
	}

	private static void insertObject(SparqlClient sparqlClient, String csvFile, String cvsSplitBy) {
		String line;
		// nbPersonnesParPiece(sparqlClient);
		System.out.println("ajout d'une personne dans le bureau:");
		String prefixPopulation = "PREFIX RECENSEMENT: <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_5c0ace4a_18fa_4172_a4d7_f3317cdf79e0>";
		String prefixAnnee = "PREFIX ANNEE <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_bc3d0556_265a_4f58_b5bb_17321bc1fbf6>";
		String prefixLieu = "PREFIX LIEU <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_51a5bd12_b945_4ba6_8b98_67f56a7f4a96>";

		String prefixeRecensement = "PREFIX RECENSEMENT:      <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_5c0ace4a_18fa_4172_a4d7_f3317cdf79e0>";

		String prefixRDFS = "PREFIX rdfs: <http://www.w3.org/2000/01/rdfs-schema#>";
		String prefixRDF = "PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>";
		String prefixOWL = "PREFIX owl:  <http://www.w3.org/2002/07/owl#>";

		String prefixAPourRecensement = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLObjectProperty_ea54c651_cd09_4455_a859_33e01977d630>";
		String prefixApourAnnee = "PREFIX : <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLDataProperty_2154ceef_5ff4_4404_b036_b6503aaeca98>";

		try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {

			while ((line = br.readLine()) != null) {

				// use comma as separator
				String[] country = line.split(cvsSplitBy);
				System.out.println(country.length + "  " + country);
				System.out.println(country.length + country[0] + " " + country[1] + " " + country[2]);

				String requestInsertLieu = prefixLieu + " " + prefixRDFS + " INSERT DATA { LIEU:" + country[0]
						+ " rdfs:label " + country[0] + "}";
				String requestInsertRecensement = prefixPopulation + " " + prefixRDFS + " " + prefixeRecensement
						+ " INSERT DATA { RECENSEMENT:" + country[1] + " rdfs:label " + country[1] + "}";
				String requestInsertAnnee = prefixAnnee + " " + prefixRDFS + " INSERT DATA { ANNEE :" + country[2]
						+ " rdfs:label " + country[2] + "}";
				String requestInsertRecenAnnne = prefixAnnee + " " + prefixRDFS + " " + prefixApourAnnee
						+ " INSERT DATA {:" + country[1] + " :a pour annee :" + country[2] + "}";

				String requestPop = prefixAnnee + " " + prefixRDFS + " " + prefixAPourRecensement + " INSERT DATA { :"
						+ country[0] + ":a pour recensement" + ":" + country[1] + "}";

				if (sparqlClient.update(requestInsertRecensement) && sparqlClient.update(requestInsertAnnee)) {
					System.out.println("here we are ");
					if (sparqlClient.update(requestInsertRecenAnnne) && sparqlClient.update(requestInsertLieu))
						sparqlClient.update(requestPop);

				}

				// query = "PREFIX : <http://www.lamaisondumeurtre.fr#>\n"
				// + "PREFIX instances: <http://www.lamaisondumeurtre.fr/instances#>\n" +
				// "INSERT DATA\n"
				// + "{\n" + " iç)nstances:Bob :personneDansPiece instances:Bureau.\n" + "}\n";

			}

		} catch (IOException e) {
			e.printStackTrace();
		}

		// nbPersonnesParPiece(sparqlClient);
	}

	private static void nbPersonnesParPiece(SparqlClient sparqlClient) {

		String query = "SELECT ?lieu ?annee ?recensement  WHERE\n" + "{\n"
				+ "    ?lieu :a pour recensement ?recensement.\n" + "}\n" + "GROUP BY ?lieu\n";
		System.err.println(query);
		Iterable<Map<String, String>> results = sparqlClient.select(query);
		System.out.println("nombre de personnes par piÃ¨ce:");
		for (Map<String, String> result : results) {
			System.out.println(result.get("lieu") + " : " + result.get("annee") + " : " + result.get("recensement"));
		}

	}
}
