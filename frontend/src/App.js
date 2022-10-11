import logo from './logo.svg';
import './App.css';
import React from "react";
import  ManagerList from './components/Manager';
import  MenuList from './components/Menu';
import  FooterList from './components/Footer';
import axios from "axios";

class App extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
        'managers': []
        }
    }

    componentDidMount() {

//        const managers = [
//            {'first_name': 'test',
//             'last_name': 'test',
//             'user_name':'test',
//             'email':'test@test.ru'
//            }
//        ]
        axios.get('http://127.0.0.1:8000/managers/').then (response => {
            this.setState( {
                'managers':response.data
            })

        }).catch(error => console.log(error))

    }


    render(){
        return (
            <div>
                <div class="wrapper"><ManagerList managers={this.state.managers} />
                    <div class="content"> <MenuList /> </div>
                    <div class="footer"> <FooterList /> </div>
                </div>
            </div>
        );
    }

}
export default App;
