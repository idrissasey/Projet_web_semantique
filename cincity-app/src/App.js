import React from "react";
import logo from "./logo.svg";
import "./App.css";

import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";

function App() {
  const useStyles = makeStyles({
    root: {
      maxWidth: 345,
    },
  });

  const classes = useStyles();

  const films = [
    {
      titre: "LaLand",
      annee: "1960",
      info: "bal bal bal ",
      image: "http://idrissaseyd.000webhostapp.com/HadithSharingImg1.jpg",
    },
    {
      titre: "Tyler",
      annee: "1960",
      info: "bal bdfdf dfd f ",
      image: "http://idrissaseyd.000webhostapp.com/HadithSharingImg2.jpg",
    },
  ];
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>

      {films.map &&
        films.map((item, i) => (
          <Card className={classes.root}>
            <CardActionArea>
              <CardMedia
                component="img"
                alt="Contemplative Reptile"
                height="140"
                image={item.image }
                title="Contemplative Reptile"
              />
              <CardContent>
                <Typography gutterBottom variant="h5" component="h2">
                  {  item.titre  + " - " + item.annee}
                </Typography>
                <Typography variant="body2" color="textSecondary" component="p">
                    {  item.info }
                </Typography>
              </CardContent>
            </CardActionArea>
            <CardActions>
       
              <Button size="small" color="primary">
                Statistique
              </Button>
            </CardActions>
          </Card>
        ))}
    </div>
  );
}

export default App;
