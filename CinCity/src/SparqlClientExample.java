
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
		nbPersonnesParPiece(sparqlClient);
		System.out.println("ajout d'une personne dans le bureau:");
		String prefixPopulation = "PREFIX RECENSEMENT: <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_5c0ace4a_18fa_4172_a4d7_f3317cdf79e0>>";
		String prefixAnnee = "PREFIX ANNEE <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_bc3d0556_265a_4f58_b5bb_17321bc1fbf6>";
		String prefixLieu = "PREFIX LIEU <http://www.semanticweb.org/nathalie/ontologies/2017/1/untitled-ontology-161#OWLClass_51a5bd12_b945_4ba6_8b98_67f56a7f4a96>";
		try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {

			while ((line = br.readLine()) != null) {

				// use comma as separator
				String[] country = line.split(cvsSplitBy);
				System.out.println(country.length + "  " + country);
				System.out.println(country.length + country[0] + " " + country[1] + " " + country[2]);

				String requestInsertLieu = prefixLieu + "INSERT DATA { LIEU:" + country[0] + " rdfs:label " + country[0]
						+ "}";
				String requestInsertRecensement = prefixPopulation + "INSERT DATA { RECENSEMENT:" + country[2]
						+ " rdfs:label " + country[2] + "}";
				String requestInsertAnnee = prefixAnnee + "INSERT DATA { ANNEE :" + country[3] + " rdfs:label "
						+ country[3] + "}";
				String requestInsertRecenAnnne = prefixAnnee + "INSERT DATA {:" + country[2] + " :a pour annee :"
						+ country[3] + "}";

				String requestPop = prefixAnnee + "INSERT DATA { :" + country[0] + ":a pour recensement" + ":"
						+ country[2] + "}";

				if (sparqlClient.update(requestInsertRecensement) && sparqlClient.update(requestInsertAnnee)) {

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

		nbPersonnesParPiece(sparqlClient);
	}

	private static void nbPersonnesParPiece(SparqlClient sparqlClient) {
		String query = "PREFIX : <http://www.lamaisondumeurtre.fr#>\n"
				+ "SELECT ?piece (COUNT(?personne) AS ?nbPers) WHERE\n" + "{\n"
				+ "    ?personne :personneDansPiece ?piece.\n" + "}\n" + "GROUP BY ?piece\n";
		Iterable<Map<String, String>> results = sparqlClient.select(query);
		System.out.println("nombre de personnes par piÃ¨ce:");
		for (Map<String, String> result : results) {
			System.out.println(result.get("piece") + " : " + result.get("nbPers"));
		}
	}
}
