import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import UsersPage from './pages/UsersPage';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/" component={UsersPage} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;