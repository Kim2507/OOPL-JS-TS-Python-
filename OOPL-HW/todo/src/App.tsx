import React from 'react';
import './App.css';
import TodoListPanel from './TodoListPanel';

/**
 * Basic React Component.
 */
class App extends React.Component{
  
  /**
   * Render JSX Content.
   * @returns JSX Element.
   */
  render(): JSX.Element {
    return(
        <div>
          <TodoListPanel />
        </div>
    );
  }
}

export default App;

