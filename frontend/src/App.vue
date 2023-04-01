<template>
  <router-view></router-view>
</template>
<script>
export default {

}
</script>

<style>
  table {
    margin: auto;
    width: 80%;
  }
  th {
    background-color: #4caf50;
    color: white;
  }
  td {
    text-align: left;
    padding: 8px;
  }
  tr:nth-child(even) {
    background-color: #f2f2f2;
  }
  button {
    background-color: #4caf50;
    border: none;
    color: white;
    padding: 10px 16px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
  }
  input {
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
  }
  label {
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
  }
  #new{
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 0;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 10px 20px;
  }
  
  #new:hover {
    background-color: #0062cc;
    color: #fff;
  }

  #edit {
    background-color: #28a745;
    color: #fff;
    border: none;
    border-radius: 0;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 10px 20px;
  }
  
  #edit:hover {
    background-color: #218838;
    color: #fff;
  }

  #delete {
    background-color: #dc3545;
    color: #fff;
    border: none;
    border-radius: 0;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 10px 20px;
  }
  
  #delete:hover {
    background-color: #c82333;
    color: #fff;
  }

  .save {
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 0;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 10px 20px;
  }
  
  .save:hover {
    background-color: #0069d9;
    color: #fff;
  }

  .cancel {
    background-color: #6c757d;
    color: #fff;
    border: none;
    border-radius: 0;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 10px 20px;
  }
  
  .cancel:hover {
    background-color: #5a6268;
    color: #fff;
  }

  .actions {
    text-align: center;
  }

  .search {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
  }
  
  .goto {
  min-width: 130px;
  height: 40px;
  color: #fff;
  padding: 5px 10px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
  outline: none;
  border-radius: 5px;
  border: none;
  background-size: 120% auto;
  background-image: linear-gradient(315deg, #833ab4 0%, #fd1d1d 50%, #fcb045);
  }
  .goto:hover {
    background-position: right center;
  }
  .goto:active {
    top: 2px;
  }

</style>