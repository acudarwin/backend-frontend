<template>
    <div>
      <input class="search" type="text" v-model="searchQuery" placeholder="Search by name"
        @input="handleChange" />
      <!--<button @click="search(searchQuery)">Search</button>-->
    </div>
</template>
  
<script>
  import { ref } from 'vue';
  
  export default {
    name: 'SearchBar',
    props: {},
    setup(props, context) {
      const searchQuery = ref();

      const search = (searchQuery) => {
        context.emit('onSearch', searchQuery);
      }

      const handleChange = (event) => {
        context.emit('onSearch', event.target.value);
      }

      return {
        searchQuery,
        search,
        handleChange,
      }
    },
  };
</script>
<style scoped>
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

  .search {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
  }

</style>