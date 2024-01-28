// function MyButton() {
//   return (
//     <button>
//       I'm a button
//     </button>
//   );
// }

// function AboutPage() {
//   return (
//     <>
//       <h1>About</h1>
//       <p>Hello there.<br />How do you do?</p>
//     </>
//   );
// }


// export default function MyApp() {
//   return (
//     <div>
//       <h1>Welcome to my app</h1>
//       <MyButton />
//       <AboutPage />
//     </div>
//   );
// }




import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';

const CreatePage = () => (
  <div>
    <h2>Create Cards</h2>
    {/* Your CreatePage component content goes here */}
  </div>
);

const PdfPage = () => (
  <div>
    <h2>Import PDF</h2>
    {/* Your PdfPage component content goes here */}
  </div>
);

const Button = ({ label, onClick }) => (
  <div style={{ margin: '20px', padding: '25px', backgroundColor: '#3A9D5D', borderRadius: '12px' }}>
    <button
      style={{
        color: 'white',
        fontWeight: 'bold',
        fontSize: '16px',
        border: 'none',
        backgroundColor: 'inherit',
        cursor: 'pointer',
      }}
      onClick={onClick}
    >
      {label}
    </button>
  </div>
);

const App = () => (
  <Router>
    <div style={{ backgroundColor: 'white' }}>
      <header>
        <h1>FlashCard Generator</h1>
      </header>

      <main style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
        <Button label="Create Cards" onClick={() => window.location.href = '/createPage'} />
        <Button label="Import PDF" onClick={() => window.location.href = '/pdfPage'} />
      </main>
    </div>

    {/* Define Routes */}
    <Route path="/createPage" component={CreatePage} />
    <Route path="/pdfPage" component={PdfPage} />
  </Router>
);

export default App;
