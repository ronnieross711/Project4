// Skater.jsx
import React, { useState, useEffect } from "react";
import DeleteSkater from "./DeleteSkater";
import DeleteButton from './DeleteButton';

function Skater(props) {
  const [skaterDetail, setSkaterDetail] = useState([]);
  console.log(props.match.params.id);

  useEffect(() => {
    fetch(`http://localhost:8000/skaters/${props.match.params.id}`)
      .then((res) => res.json())
      .then((result) => {
        setSkaterDetail(result);
        console.log(result);
        console.log(skaterDetail)
      })

      .catch(console.error);
  }, []);

  return (
    <div>
      {/* <img src={skaterDetail.photo_url} alt={skaterDetail.id}/> */}
      <h3>Name: {skaterDetail.name}</h3>
      <h3>Age: {skaterDetail.age}</h3>
      <h3>Hometown: {skaterDetail.home_town}</h3>
      <h3>Sponsor: {skaterDetail.board_sponsor}</h3>
      <h3>Shoe Sponsor: {skaterDetail.shoe_sponsor}</h3>
      <DeleteButton skaterId={skaterDetail.id}/>
    </div>
  );
}

export default Skater;

// Main.jsx

import React from "react";
import Create from "./Create";
import Home from "./Home";
import Skaters from "./Skaters";
import Login from "./Login";
import CreateSkaters from './CreateSkater';
import { Link, Route } from "react-router-dom";
import Skater from "./Skater";

function Main(props) {
  return (
    <div>
      <Route exact path="/" component={Home} />
      <Route exact path="/create" component={Create} />
      <Route exact path="/createskaters" component={CreateSkaters} />
      <Route exact path="/login" component={Login} />
      <Route exact path="/skaters" component={Skaters} />
      <Route exact path="/skaters/:id" component={Skater} />
      
    </div>
  );
}

// const Login = {
//     userName = '',
//     password = '',
// }

export default Main;


import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";




// Skaters.jsx
function Skaters(props) {
  const [skaters, setSkaters] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/skaters/")
      .then((result) => result.json())

      .then((result) => {
        setSkaters(result);
        console.log(result);
      })

      .catch(console.error);
  }, []);

  return (
    <section class="container">
      {skaters.map((skater) => {
        return (
          <div class="card-title">
            <Link to={`/skaters/${skater.id}`} key={skater.id}>
              <div class="card-image">
                <img src={skater.photo_url} alt="" />
              </div>
              <h3>{skater.name}</h3>
            </Link>
            
          </div>
        );
      })}
      
    </section>
  );
}

export default Skaters;



