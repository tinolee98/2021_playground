//import logo from './logo.svg';
//import './App.css';

import React from "react";
import axios from "axios";

class App extends React.Component{
  state = {
    isLoading: true,
    movies: [] 
  };
  componentDidMount() {
    const movies = axios.get("https://yts-proxy.now.sh/list_movies.json");
  }
  render(){
    const {isLoading} = this.state;
    return (
    <div>
      {isLoading ? "Loading..." : "We are ready!"}
      <h1>the number is {this.state.count}</h1>
      <button onClick={this.plus}>Plus</button>
      <button onClick={this.minus}>Minus</button>
    </div>
    );
  }
}



export default App;