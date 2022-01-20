import React from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import MenuItemList from './components/Menu.js'
import ShowFooter from './components/Footer.js'
import ProjectList from './components/Projects.js'
import TODOList from './components/TODOs.js'
import { BrowserRouter, Route, Link, Routes, Navigate } from 'react-router-dom'

const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница не найдена</h1>
        </div>
    )
}

class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects': [],
           'todo': [],
           'menu': [],
       }
   }


   componentDidMount() {
       axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data.results;
                this.setState({
                    'users': users,
                    'menu': this.state.menu
                });
            })
            .catch(error => console.log(error))

       axios.get('http://127.0.0.1:8000/api/projects/')
           .then(response => {
               const projects = response.data.results
               this.setState(
                   {
                       'projects': projects,
                   }
                )
           }).catch(error => console.log(error))

       axios.get('http://127.0.0.1:8000/api/TODO/')
           .then(response => {
               const todos = response.data.results
               this.setState(
                   {
                       'todos': todos,
                   }
                )
           }).catch(error => console.log(error));

       this.setState({
           'users': this.state.users,
           'menu': [
               {
                   'name': 'Пользователи',
                   'url': 'http://localhost:8000/'
               }
            ],
           'projects': [
               {
                  'name': 'Проекты',
                   'url': 'http://localhost:8000/'
               }
           ],
           'todos': [
               {
                   'name': 'TODO',
                   'url': 'http://localhost:8000/'
               }
           ]
       })
   }


render() {
        return (
            <div class="wrapper">
                <div class="top">
                    <div class="main_blocks_container">
                        <BrowserRouter>
                            <div class="left_block">
                                <div class="menu">
                                    <MenuItemList menu={this.state.menu} />

                                </div>
                            </div>
                            <div class="right_block">
                                <div class="content">

                                    <Routes>
                                        <Route exact path='/' element={<UserList users={this.state.users} />} />
                                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />} />
                                        <Route exact path='/TODO' element={<TODOList todos={this.state.todos} />} />
                                        <Route path="/users" element={<Navigate replace to="/" />} />
                                        <Route path='*' element={<NotFound404 />} />
                                    </Routes>

                                </div>
                            </div>
                        </BrowserRouter>
                    </div>
                </div>

                <div class="footer">
                    <ShowFooter showFooter={this.state.showFooter} />
                </div>
            </div>
        )
   }
}


export default App;