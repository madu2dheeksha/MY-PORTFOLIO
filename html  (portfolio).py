<!DOCTYPE html>
<html>
<head>
    <title>Python Developer Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <script> // Add event listener to navigation links
        document.querySelectorAll('nav a').forEach((link) => {
            link.addEventListener('click', (event) => {
                event.preventDefault();
                const id = link.getAttribute('href').replace('#', '');
                document.querySelector(`#${id}`).scrollIntoView({ behavior: 'smooth' });
            });
        }); </script> 
    <header>
        <h1> Madu Dheeksha's Portfolio</h1>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="about">
            <h2>About Me</h2>
            <p> Hello I'm Dheeksha , 1st year undergraduate student , interested in technology. 
                Finding interest in all the tech skills like UI/UX design, web developing , 
                working upon databases and also very much passionated about learning booming technologies like Machine Learning, Data science with Artificial Intelligence .  
                I had completed few internships upon basic E-Commerce website designing .  </p>
            
        </section>
        <section id="projects">
            <h2>Projects</h2>
            <ul>
                <li>
                    <h3>Project 1: PortFolio </h3>
                    <p> Making Portfolio of my skills and experience.</p>
                    <img src ="dheeksha port.png" alt="portfolio">
                    

                </li>
                <li>
                    <h3>Project 2: To-Do List</h3>
                    <p> To-Do List built using HTML and CSS .</p>
                    <img src="dolist.image.webp" alt="Web Scraper">
                </li>
                <li> 
                    <h3>Project 3: Login form  </h3>
                    <p> A demo login form for login or sinup.</p>
                    <img src ="loginform.image.png" alt="Loginform">
                </li>
                <li> 
                    <h3>Project 4: Chat-Bot  </h3>
                    <p> A simple chatbot built using Python and the NLTK library.</p>
                    <img src ="chatbot.photo.jpg" alt="Chat-Bot">
                </li>
            </ul>
        </section>
        <section id="skills">
            <h2>Skills</h2>
            <ul>
                <li> C,C#,C++</li> <br> <img src="c.image.jpg" alt="c ">
                <li>Python</li>  <br> <img src="python.iamge.jpg" alt="python">
                <li>JavaScript</li> <br> <img src="js.iamge.webp" alt="JS ">
                <li>HTML/CSS</li> <br> <img src="HTMLand css.image.webp" alt="HTML/CSS ">
                <li>Machine Learning</li> <br> <img src="machine learning.image.jpg" alt="c ">
            </ul>
        </section>
        <section id="contact">
            <h2>Contact</h2>
            <p>Get in touch with me:</p>
            <ul>
                <li><a href="https://www.linkedin.com/in/madu-dheeksha/">LinkedIn</a></li>
                <li><a href= "https://github.com/madu2dheeksha/">Github</a></li>
                <li><a href="mailto:deeksham881@gmail.com">deeksham881@gmail.com</a></li>
                
            </ul>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Python Developer Portfolio</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
