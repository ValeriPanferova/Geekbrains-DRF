import React from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import MenuItemList from './components/Menu.js';
import ShowFooter from './components/Footer.js';


class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'menu': []
       }
   }


   componentDidMount() {
       axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data;
                this.setState({
                    'users': users,
                    'menu': this.state.menu
                });
            })
            .catch(error => console.log(error));

       this.setState({
           'users': this.state.users,
           'menu': [
               {
                   'name': 'Главная',
                   'url': 'http://localhost:8000/'
               }
            ]
        });
    }

   render () {
        return (
            <div>
                <div>
                    <MenuItemList menu={this.state.menu} />
                </div>
                <div>
                    <UserList users={this.state.users} />
                </div>
                <div>
                    <ShowFooter />
                </div>
            </div>
        )
    }
}


export default App;