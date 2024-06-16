<style> body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
    }
    .container {
  height: 500px; /* any fixed value for the parent */
}

.img {
  width: auto;
  height: 100%;
  aspect-ratio: 1; /* will make width equal to height (500px container) */
  object-fit: cover; /* use the one you need */
}
    
    header {
        background-color:black;
        color: #fff;
        padding: 1em;
        text-align:center;
    }
    
    nav ul {
        list-style: none;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: space-between;
    }
    
    nav li {
        margin-right: 20px;
    }
    
    nav a {
        color: #fff;
        text-decoration: none;
    }
    
    nav a:hover {
        color:beige;
    }
    
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 2em;
    }
    
    section {
        background-color:ivory;
        padding: 2em;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    h2 {
        margin-top: 0;
    }
    
    img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
    }
    
    footer {
        background-color: #333;
        color: #fff;
        padding: 1em;
        text-align: center;
        clear: both;
    }</style>
