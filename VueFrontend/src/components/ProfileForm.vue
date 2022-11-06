<script>
export default {
	props: [
		"type",
		"profileid"
	],
	data() {
		return {
			name: "",
			date_of_birth: "",
			age: 0,
			email: "",
			accepted: false,
		};
	},
	methods: {
		async submitcharacterinfo(event) {
			let response = await fetch("http://localhost:8000/addprofile", {
				method: "POST",
				headers: {
					"content-type": "application/json;charset=utf-8",
				},
				body: JSON.stringify({
					name: this.name,
					age: this.age,
					date_of_birth: this.date_of_birth,
					email: this.email,
				}),
			});
			
			this.accepted = response.ok;
			if (this.accepted) {
				this.name = "";
				this.date_of_birth = "";
				this.age = 0;
				this.email = "";
			}
		},
		async getprofileinfo()
        {
            let response = await fetch("http://localhost:8000/getprofiles?profileid=" + this.profileid);
            let profile = await response.json();
            
			this.name = profile["name"];
			this.age = profile["age"];
			this.date_of_birth = profile["date of birth"];
			this.email = profile["email"];
        },
		async editprofile()
		{
			let response = await fetch("http://localhost:8000/editprofile", {
				method: "PUT",
				headers: {
					"content-type": "application/json;charset=utf-8",
				},
				body: JSON.stringify({
					id: this.profileid,
					name: this.name,
					age: this.age,
					date_of_birth: this.date_of_birth,
					email: this.email,
				}),
			});

			this.accepted = response.ok;
		},
		nameinputhandler(event) {
			this.name = event.target.value;
		},
		ageinputhandler(event) {
			this.age = event.target.value;
		},
		datebirthinputhandler(event) {
			this.date_of_birth = event.target.value;
		},
		emailinputhandler(event) {
			this.email = event.target.value;
		},
	},
	mounted()
	{
		if (this.type == "edit")
		{
			this.getprofileinfo();
		}
	}
};
</script>

<template>
	<form class="container mt-4">
		<h2 v-if="type == 'edit'" class="text-center"><u>Edit this character profile</u></h2>
		<h2 v-else class="text-center"><u>Enter Your New Fictional Character</u></h2>
		<label class="form-label"><b>Name: {{ name }}</b></label>
		
		<input
			class="form-control"
			name="name"
			type="text"
			@input="nameinputhandler"
			:value="this.name"
		/>
		
		<label class="form-label"><b>age: {{ age }}</b></label>
		
		<input
			class="form-control"
			name="age"
			type="number"
			@input="ageinputhandler"
			:value="this.age"
			min="0"
		/>
		
		<label class="form-label"><b>Date of Birth: {{ date_of_birth }}</b></label>
		
		<input
			class="form-control"
			name="date_of_birth"
			type="date"
			@input="datebirthinputhandler"
			:value="this.date_of_birth"
		/>
		
		<label class="form-label"><b>Email: {{ email }}</b></label>
		
		<input
			class="form-control mb-5"
			name="email"
			type="email"
			@input="emailinputhandler"
			:value="this.email"
		/>
		
		<div class="row">
			<button class="col btn btn-dark" v-if="type == 'edit'" @click.prevent="editprofile">Confirm Edit</button>
			<button class="col btn btn-dark" v-else @click.prevent="submitcharacterinfo">Submit</button>
		</div>
	</form>

	<h1 v-if="this.accepted && type == 'edit'">Character Updated</h1>
	<h1 v-else-if="this.accepted">Character Submited</h1>
</template>
