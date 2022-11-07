<script>
import ProfileForm from "./components/ProfileForm.vue"

export default {
    components: {
        ProfileForm
    },
	data() {
		return {
            isadd: false,
            isedit: false,
            editprofileid: 0,
			characters: [],
            responded: false
		};
	},
	methods: {
        removeinarray(id)
        {
            let newcharacters = [];
            this.characters.forEach(character => {
                if (character["id"] != id)
                {
                    newcharacters.push(character);
                }
            });

            this.characters = newcharacters;
        },
		async getcharacterinfos() {
			let response = await fetch("http://localhost:8000/getprofiles");
			let profiles = await response.json();

            this.characters = profiles["profiles"];
		},
        async deleteprofile(event)
        {
            let response = await fetch("http://localhost:8000/deleteprofile",{
                method: "DELETE",
                headers: {
					"content-type": "application/json;charset=utf-8",
				},
                body: JSON.stringify(
                    {
                        id: event.target.value
                    })
            });

            if (response.ok)
            {
                this.removeinarray(parseInt(event.target.value));
            }
        },
        toform(event)
        {
            this.isadd = true;
        },
        tolist(event)
        {
            this.isadd = false;
            this.isedit = false;
            this.getcharacterinfos();
        },
        toedit(event)
        {
            this.isedit = true;
            this.editprofileid = event.target.value;
        }
	},
	mounted() {
		this.getcharacterinfos();
	}
};
</script>

<template>
    <header class="container-md">
        <div class="row mb-4">
            <h1 class="title col text-center"><b><u>Fictional Characters</u></b></h1>
        </div>
    </header>
    <nav class="container-md">
        <div class="row">
            <button class="col me-2 btn btn-dark" @click="toform">Enter a new character</button>
            <button class="col ms-2 btn btn-dark" @click="tolist">List of Fictional Characters</button>
        </div>
    </nav>
    
    <ProfileForm v-if="isadd" type="add"/>
    <ProfileForm v-else-if="isedit" type="edit" :profileid="editprofileid" />
    <section v-else v-for="char in characters" class="container-md float">
        <template v-for="(prop, key) in char">
            <div v-if="key !== 'id'" class="row my-1">
                <p class="col border rounded border-3 border-primary ms-2 text-center fs-3">
                    {{ key }}: {{ prop }}
                </p>
            </div>
        </template>
        <div class="row mb-4">
            <button :value="char['id']" class=" col me-2 btn btn-dark" @click="toedit">Edit this profile of {{ char["name"] }}</button>
            <button :value="char['id']" class=" col btn btn-dark text-wrap" @click="deleteprofile"> Delete this character</button>
        </div>
	</section>
</template>
