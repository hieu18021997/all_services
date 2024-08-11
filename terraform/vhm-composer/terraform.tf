terraform {
	required_providers {
		google = {
		source  = "hashicorp/google"
		version = "5.10.0"
		}
	}
}

provider "google" {
	project = "vhm-dataops-prod"
	region  = "asia-southeast1"
	zone    = "asia-southeast1-a"
}

resource "google_composer_environment" "vhm-composer" {
	provider = google
	name     = "vhm-composer"
	region   = "asia-southeast1"
	labels = {
		"environment_name" = "vhm-composer"
		"owner"            = "vhm"
	}

	config {
		software_config {
			image_version = "composer-2.6.2-airflow-2.6.3"
			airflow_config_overrides = {
				"core-airflow_home" = "/home/airflow/gcs"
			}
			pypi_packages = {
				numpy = ""
				simple_salesforce = ""
				python-dotenv = ""
				fastparquet = ""
				pysftp = ""
				pyodbc = ""
				pymsteams = ""
				jsonschema = ""
				hdbcli = ""
				openpyxl = ""
				facebook-business = ""
				google-ads = ""
				unidecode = ""
				joblib = ""
			}
		}
		# workloads_config {
		# 	scheduler {
		# 	  count = 2
		# 	  cpu = 2
		# 	  memory_gb = 2
		# 	  storage_gb = 3
		# 	}
		# 	triggerer {
		# 	  count = 1
		# 	  cpu = 0.5
		# 	  memory_gb = 0.5
		# 	}
		# 	web_server {
		# 	  cpu = 2
		# 	  memory_gb = 2
		# 	  storage_gb = 5
		# 	}
		# 	worker {
		# 		cpu = 3
		# 		memory_gb = 6
		# 		min_count = 2
		# 		max_count = 6
		# 		storage_gb = 10
		# 	}
		# }
		environment_size = "ENVIRONMENT_SIZE_MEDIUM"

		private_environment_config {
			enable_private_endpoint = true
			# enable_privately_used_public_ips = false
			# master_ipv4_cidr_block = "172.16.0.0/28"
		}


		node_config {
			network         = "projects/vhm-dataops-prod/global/networks/vhm-network-prd"
			subnetwork      = "projects/vhm-dataops-prod/regions/asia-southeast1/subnetworks/vhm-primary-subnet"
			service_account = "vhm-etl-data@vhm-dataops-prod.iam.gserviceaccount.com"
			# enable_ip_masq_agent = true
			# disk_size_gb = 100
			# zone = "asia-southeast1-a"
			ip_allocation_policy {
				cluster_secondary_range_name  = "vhm-secondary-pod"
				services_secondary_range_name = "vhm-secondary-service"
			}
			# ip_allocation_policy = [{
			# 	use_ip_aliases = true
			# 	// Other networking configuration
			# }]
			enable_ip_masq_agent = true    
			# ip_allocation_policy = [{
			# use_ip_aliases = true
			# cluster_secondary_range_name = "vhm-secondary-pod"
			# services_secondary_range_name = "vhm-secondary-service"
			# cluster_ipv4_cidr_block = "10.243.56.0/21"
			# services_ipv4_cidr_block = "10.243.54.64/27"
			# # cluster_ipv4_cidr_block = "10.243.56.0/21"
			# # services_ipv4_cidr_block = "10.243.54.64/27"
			# # services_ipv4_cidr_block = "172.16.40.0/23"
			# }]
		}

		

		

		# private_environment_config {
		#   enable_private_endpoint = false
		#   connection_type = "PRIVATE_SERVICE_CONNECT"
		#   cloud_composer_connection_subnetwork = "projects/vhm-dataops-prod/regions/asia-southeast1/subnetworks/vhm-primary-subnet"
		#   # cloud_composer_network_ipv4_cidr_block = "172.31.235.0/24"
		#   # cloud_sql_ipv4_cidr_block = "10.0.0.0/12"
		# }

		
	}
}
