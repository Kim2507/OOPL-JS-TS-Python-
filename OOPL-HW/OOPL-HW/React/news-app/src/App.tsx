import React from 'react';
import Card from './NewsBox';
import './App.css';
import NewsBox from './NewsBox';

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
        <NewsBox/>
        <NewsBox/>
      </div>
    );
  }
}

export default App;