import React from "react";

interface HeaderProps {
  notification?: number;
}

let Header = (props: any) => {
  return (
    <nav
      className="navbar is-transparent"
      role="navigation"
      aria-label="main navigation"
    >
      <div className="navbar-brand">
        {props.SidebarToggler}
      </div>

      <div className="navbar-menu">
        <div className="navbar-start">
          <div className="navbar-item is-hoverable">
            <a href="/#" className="navbar-item">
              Home
            </a>
          </div>
          <div className="navbar-item is-hoverable">
            <a href="/#" className="navbar-item" onClick={() => {
              window.open("https://github.com/jiajunmao/4641-Project", "_blank"); 
            }}>
              Documentation
            </a>
          </div>
        </div>

        <div className="navbar-end">
          <div className="navbar-item">
            <div className="buttons">
              <a href="/#" className="button is-primary">
                <strong>Sign up</strong>
              </a>
              <a href="/#" className="button is-light">
                Log in
              </a>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Header;
