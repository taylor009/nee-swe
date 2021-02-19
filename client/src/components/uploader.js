import React from 'react';

class Uploader extends React.Component {
    constructor(props) {
    super(props);

    this.handleUpload = this.handleUpload.bind(this);
  }

  handleUpload(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);

    fetch('http://34.72.94.167:80/upload', {
      method: 'POST',
      body: data,
    }).then((response) => {
        if (response.status === 200){
            alert("File Uploaded Successfully");
        }
        else {
            alert("Error Uploading file")
        }
    });
  }

  render() {
    return (
      <form onSubmit={this.handleUpload}>
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
        </div>
        <br />
        <div>
          <button>Upload</button>
        </div>
      </form>
    );
  }
}

export default Uploader;