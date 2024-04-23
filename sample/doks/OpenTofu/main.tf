resource "digitalocean_kubernetes_cluster" "primary" {
  name         = var.doks_cluster_name
  version      = var.doks_cluster_version
  region       = var.do_region
  auto_upgrade = var.auto_upgrade

  node_pool {
    name       = "${var.doks_cluster_name}-pool"
    size       = var.doks_cluster_pool_size
    node_count = var.doks_cluster_pool_node_count
    auto_scale = true
    min_nodes  = var.doks_cluster_autoscale_min
    max_nodes  = var.doks_cluster_autoscale_max

    tags       = [ var.do_region, 
                   var.doks_cluster_name ]

    labels     = { "region": var.do_region,
                   "cluster_name": var.doks_cluster_name }

  }

  tags         = [ var.do_region, 
                   var.doks_cluster_name ]

}
