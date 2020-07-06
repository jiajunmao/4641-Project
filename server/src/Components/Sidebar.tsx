import React from "react";


interface SidebarProps {
  username: String;
  avatar: string;
}

let Sidebar = (props: any) => {
  return (
    <div className="SidebarContainer box">
      <div className="card">
        <div className="card-content">
          <div className="media">
            <div className="media-left">
              <figure className="image is-64x64">
                <img className="is-rounded" src={props.avatar} alt="avatar" />
              </figure>
            </div>
            <div className="media-content">
              <p className="title is-4">{props.username}</p>
              <div className="subtitle is-6">{props.jobtitle}</div>
            </div>
          </div>
          <div className="logoContent">
            <figure className="image is-32x32 LogoContainer">
              <img
                className="is-rounded logo"
                src={process.env.PUBLIC_URL + "/img/fb.svg"}
                alt="avatar"
              />
            </figure>
            <figure className="image is-32x32 LogoContainer">
              <img
                className="is-rounded logo"
                src={process.env.PUBLIC_URL + "/img/linkedin.svg"}
                alt="avatar"
              />
            </figure>
            <figure className="image is-32x32 LogoContainer">
              <img
                className="is-rounded logo"
                src={process.env.PUBLIC_URL + "/img/twitter.svg"}
                alt="avatar"
              />
            </figure>
          </div>
        </div>
      </div>
      <div className="menu">
        <p className="menu-label">Main Menu</p>
        <ul className="menu-list">
          <li>
            <a href="/#">DashBoard</a>
          </li>
          <li>
            <a href="/#">
              Report
            </a>
            <ul>
              <li>
                <a href="/#">View Your Report</a>
              </li>
              <li>
                <a href="/#" onClick={props.uploader}>Generate new Report</a>
              </li>
            </ul>
          </li>
          <li>
            <a href="/#">Connect to Cloud</a>
          </li>
        </ul>
      </div>
      <footer className="footer">
          <div className="content has-text-centered">
            <p>
              <strong>My-App</strong> by{" "}
              <a href="/#">Wei Xin</a>.
            </p>
          </div>
        </footer>
    </div>
  );
};

export default Sidebar;
