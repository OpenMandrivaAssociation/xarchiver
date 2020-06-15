Summary:	A lightweight archiving/compression tool
Name:		xarchiver
Version:	0.5.4.15
Release:	1
License:	GPLv2
Group:		Archiving/Compression
URL:		http://xarchiver.xfce.org
Source0:	https://github.com/ib/xarchiver/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	desktop-file-utils
BuildRequires:  xsltproc

Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
#Requires:	binutils
Requires:	unzip
Requires:	zip
Recommends:	arj
Recommends:	p7zip
Recommends:	lha
Recommends:	unrar
Recommends:	xz

%description
Xarchiver is a GTK+2 only frontend to 7z, zip, rar, tar, bzip2, gzip, arj,
lha, rpm and deb (open and extract only).Xarchiver allows you to create,
add, extract and delete files in the above formats. 7z, zip, rar, arj 
password protected archives are supported.

%prep
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

%find_lang %{name} --with-gnome %{name}.lang

# make the .desktop file compliant with xdg specs

desktop-file-install \
		--vendor="" \
		--remove-key="Encoding" \
		--remove-mime-type="multipart/x-zip" \
		--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/xarchiver.desktop


%files -f %{name}.lang
%{_bindir}/%{name}
%{_mandir}/man1/xarchiver.1.*
%{_docdir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_libexecdir}/thunar-archive-plugin/xarchiver.tap
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
