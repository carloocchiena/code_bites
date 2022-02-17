<?php
/**
 * Description: Esempio di Plugin per aggiungere colonne a Woocommerce
 * Version: 1.0.0
 * Author URI: https://thomascocchiara.it
 *
 * Text Domain: carlo
 *
 * @package carlo
 * @category Core
 *
 */

function add_nemo_column( $columns ){
	$columns['nemo'] = '';
	return $columns;
}


add_filter( 'manage_edit-product_columns', 'add_nemo_column', 9999 );

function add_nemo_column_tag( $column ) {
	if ( $column === 'nemo' ) {
		echo '<span style="padding:5px;background-color:#40519F;border-radius:5px;color:white">Nemo</span>';
	}
}

add_filter( 'manage_product_posts_custom_column', 'add_nemo_column_tag', 10, 1 );
